from flask import Flask

from board import pages

#This was the first way it was done
# app = Flask(__name__)

#functions like these are called views in flask
# @app.route("/")
# def home():
#    return "Hello, World!"

# if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8000, debug=True)


def create_app():
    app: Flask = Flask(__name__)

    app.register_blueprint(pages.bp)

    return app


