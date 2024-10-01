import flask

import flask_login

from flask import *

import logging
import datetime
import os

app = flask.Flask(__name__,static_url_path='', 
            static_folder='static',)


login_manager = flask_login.LoginManager()
login_manager.init_app(app)

logger = logging.getLogger('werkzeug')
# Configure the logger
logging.basicConfig(format='%(asctime)s %(message)s')


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(f"The requested route {request.path} is not found")
    return "Sorry the request page is not found", 404

@app.route('/', methods=['GET', 'POST'])
def home():
    logger.info(f'- Going to make GET request on {request.path} path')
    if flask.request.method == 'GET':
        return render_template('slides.html')

app.run('0.0.0.0',debug=True,port=80)

