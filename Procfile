web: flower -A scraper.celery --address=0.0.0.0 --port=$PORT
worker: celery worker -E --app=scraper.celery