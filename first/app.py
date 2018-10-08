import views, contact, db
from flask import Flask


def create_app():
    app = Flask(__name__)
    # configurar extensões
    db.configure(app)
    views.configure(app)
    contact.configure(app)  # para usar Blueprint
    admin.configure(app)

    # configurar variáveis
    app.config['SECRET_KEY'] = 'sjiskfhlkdsfhiagfhfuc'
    return app
