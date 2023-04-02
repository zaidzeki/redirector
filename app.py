#!/usr/bin/env python3
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/<path:path>')
def index(path):
	return redirect(path)

if __name__=='__main__':
	app.run(host="::", port=10000)
