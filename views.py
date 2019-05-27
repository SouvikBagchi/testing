from flask import Flask, url_for, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    
    if request.method == 'GET':
        
        return render_template('home.html')


@app.route('/jokes',methods = ['GET','POST'])
def recommend_joke():
    '''
    session - user_pref, joke_num(0-19)
    '''
    #write code to get the first joke and compute the matrix
    
    
    joke = 'first joke'
    
    if request.method == 'GET':
        
        #we will randomly select one of the highest rated joke and display it
        #insert code to get the joke

        session['joke_num'] = 0 #this is default but you will need to get the joke number you are displaying
        return render_template('joke.html', joke= joke)
    
    else:

        #
        
        #check if session is set
        if 'user_pref' in session:

            pass

        else :

            value = request.form["rating"]

            #create a list
            #calculate svd

            #store in session
            return render_template('recommended_jokes.html', joke= "recommended joke")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    debug = True