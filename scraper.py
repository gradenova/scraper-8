import re
from dateutil.parser import parse
from xml.sax.saxutils import unescape

import requests
import bs4
from celery import Celery

from app import app, db
from models import Result


base_scraper_url = app.config.get('SCRAPER_BASE_URL')
base_url = app.config.get('BASE_URL')
base_dict = {}


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


def clean_html(html):
    return ' '.join(re.findall(r'\S+', html))


def get_rows(url):

    page = requests.get(url)
    rows = []

    if page.ok:

        content = clean_html(page.content)

        tree = bs4.BeautifulSoup(content, 'lxml')
        table = tree.find('table', class_='data')

        rows = table.find_all('tr')

    return rows


def get_article(url):

    page = requests.get(url)

    if page.ok:
        content = clean_html(page.content)
        tree = bs4.BeautifulSoup(content, 'lxml')

        return tree
    return None


@celery.task
def scraper():

    print('About to start the scraper.')

    base_rows = get_rows(base_scraper_url)
    base_for_today = base_rows[0]

    base_datacells = base_for_today.find_all('td')
    today_url_cell = base_datacells[0].find('a')

    base_dict['url'] = unescape(base_url + today_url_cell.attrs['href'])
    base_dict['date'] = parse(today_url_cell.text)

    todays_rows = get_rows(base_dict.get('url'))

    for row in todays_rows:

        datacells = row.find_all('td')

        doc = {
            'url': base_dict.get('url'),
            'date': base_dict.get('date'),
            'source': datacells[1].text,
            'agency': datacells[2].text,
            'fsg': datacells[3].text,
            'title': datacells[4].text,
            'keywords': datacells[5].text,
            'url_2': unescape(
                base_url + datacells[4].find('a').attrs.get('href')),

        }

        article = get_article(doc.get('url_2'))

        if article:
            try:
                doc['description'] = article.html

                result = Result(**doc)

                db.session.add(result)
                db.session.commit()
            except Exception as e:
                doc['description'] = article.body.text

                result = Result(**doc)

                db.session.add(result)
                db.session.commit()
            else:
                result = Result(**doc)

                db.session.add(result)
                db.session.commit()

    print('Scraper completed execution')
    return True


scraper.apply_async()
