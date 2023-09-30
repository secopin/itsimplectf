#!/usr/bin/python3
import db

from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='',static_folder='static/')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        query=db.get_all()
        return render_template("index.html",result=query,count=len(query))
    elif request.method == 'POST':
        vacancy = request.form['vacancy']
        if 'sqlmap' in request.headers.get('User-Agent'):
            query=db.get_all()
            return render_template("index.html",result=query,count=len(query))
        try:
            query = db.get_vacancies(vacancy)
            return render_template("index.html",result=query,count=len(query))
        except:
            query=db.get_all()
            return render_template("index.html",result=query,count=len(query))

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=80)

