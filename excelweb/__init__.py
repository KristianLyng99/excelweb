from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['EXCEL_FOLDER'] = 'spreadsheets'

    from . import app as app_module
    app.register_blueprint(app_module.bp)

    return app
