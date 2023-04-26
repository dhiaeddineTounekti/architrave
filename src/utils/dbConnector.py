import os
from mongoengine import connect


def connect_to_dbs() -> None:
    """
    Looks for the DB_URLS environment variable and connects to all databases.
    """
    db_urls = os.environ.get("DB_URLS")
    if not db_urls:
        raise Exception("DB_URLS environment variable must be set")
    for db_url in db_urls.split(","):
        db_url = db_url.strip()
        connect(host=db_url)
