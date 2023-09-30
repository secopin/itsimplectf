#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template
import pdfkit

app = Flask(__name__,static_url_path='',static_folder='static/')

@app.route('/pdf', methods = ['POST'])
def pdf():
    url = request.form['url']
    if url == '':
        url = 'http://127.0.0.1:80/example/example.html'
    pdf = pdfkit.from_url(url, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

