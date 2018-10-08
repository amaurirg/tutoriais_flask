from tinymongo import TinyMongoClient


def get_db():
    conn = TinyMongoClient()    # pode se passar o caminho do arquivo db ("")
    db = conn.my_database   # my_database é o nome do arquivo json do db
    return db


def configure(app):
    app.db = get_db()
