from flask import jsonify
from flask import render_template


def configure(app):
    @app.route("/")
    def hello():
        return "Hello World!!!"


    @app.route("/api")
    def api_json():
        return jsonify(data={'name': 'Amauri'})

    @app.route("/langs")
    def langs():
        languages = ['Python', 'Bash', 'Lua', 'Rust']
        return render_template('index.html',
                               title="Melhores Linguagens",
                               linguagens=languages
                               )
