from flask import render_template, request, jsonify

from app import app
from .models import *


@app.route('/')
@app.route('/index')
def index():
	message = "You're up and running."
	
	return render_template('index.html', message = message)