import os
import pandas as pd
from flask import Blueprint, current_app, render_template, send_from_directory
from werkzeug.utils import secure_filename

bp = Blueprint('excelweb', __name__)

@bp.route('/')
def index():
    folder = current_app.config['EXCEL_FOLDER']
    files = sorted(f for f in os.listdir(folder) if f.lower().endswith('.xlsx'))
    return render_template('index.html', files=files)

@bp.route('/sheet/<path:filename>')
def sheet(filename):
    folder = current_app.config['EXCEL_FOLDER']
    filename = secure_filename(filename)
    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        return 'File not found', 404
    df = pd.read_excel(filepath)
    table = df.to_html(classes='table table-striped', index=False)
    return render_template('sheet.html', table=table, filename=filename)

@bp.route('/spreadsheets/<path:filename>')
def download(filename):
    folder = current_app.config['EXCEL_FOLDER']
    filename = secure_filename(filename)
    return send_from_directory(folder, filename, as_attachment=True)
