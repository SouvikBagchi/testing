from flask import Flask, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    
    if request.method == 'GET':
        
        return render_template('home.html')
#    else :
#        return redirect(url_for('recommend_joke'))


@app.route('/firstjoke',methods = ['GET','POST'])
def recommend_joke():
    
    #write code to get the first joke and compute the matrix
    
    
    joke = 'first joke'
    
    if request.method == 'GET':
        
    
        return render_template('joke.html', joke)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)