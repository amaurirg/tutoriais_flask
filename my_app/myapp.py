import views, db
from flask import Flask


def create_app():
    app = Flask(__name__)
    views.configure(app)
    db.configure(app)
    return app
