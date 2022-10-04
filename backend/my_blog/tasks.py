from config.celery import app

from .models import Article


@app.task
def delete_post():
    try:
        Article.objects.first().delete()
    except AttributeError:
        pass
