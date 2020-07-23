import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import sys

from generate_unconditional_samples import sample_model

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b4851f2075cc425536ff1b6253b13aa4'

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/haiku',methods = ['POST'])
def haiku():
	samples = sample_model(model_name = 'train2')
	samples = ''.join(samples.split('<|endoftext|>\n'))

	return render_template('index.html', generated_haiku = samples)


if __name__ == "__main__":
	app.run(debug = True)
	# app.run(host = '0.0.0.0', port = 8080,debug=True)	