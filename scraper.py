import requests
import bs4

from app import app


base_url = app.config.get('SCRAPER_BASE_URL')


def scraper():

    base_page = requests.get(base_url)

    if base_page.ok:
        return True
