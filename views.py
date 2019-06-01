from flask import Flask, url_for, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd
import random
import pymysql
from sqlalchemy.orm import sessionmaker
from test import Com
from settings import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


app = Flask(__name__)
app.secret_key = 'verysecretsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

@app.route('/', methods = ['GET','POST'])
def hello_world():
    import models
    test = models.Test(joke = 5)
    #add to db and print
    db.session.add(test)
    db.session.flush()

    if test.id :
        db.session.commit()
        db.session.close()
        print('Comiited')

    # db.session.query()

    if request.method == 'GET':
        
        return render_template('home.html')


@app.route('/jokes',methods = ['GET','POST'])
def recommend_joke():
    '''
    session - user_pref, joke_num(0-19)
    '''
    #write code to get the first joke and compute the matrix
    
    
    joke = 'jhkgjkhgjkg jhkg '

    
    if request.method == 'GET':
        
        #we will randomly select one of the highest rated joke and display it
        #insert code to get the joke

        session['joke_num'] = random.randint(1,90) #this is default but you will need to get the joke number you are displaying
        return render_template('joke.html', joke= joke)
    
    else:

        #This is the value which the user gave to the previous joke which is represented by joke_num
        value = request.form["rating"]
        session.pop('rating',None)
        #get the joke_num
        last_joke = session['joke_num']
        session.pop('joke_num',None)
    
    
        #now that we have the joke number we will create the svd with this information
        
        #check if session is set
        if 'user_pref' in session:

            curr_user_pref = list(session['user_pref'])
            
            session.pop('user_pref',None)
            
            curr_user_pref[last_joke] = value
            
            #fetch the data
            #create the matrix
            #append the user_pref
            #calculate svd
            
            new_joke = 'new joke'
            new_joke_number = random.randint(1,90)#needs to be the one that is being recommend_joke
            
            #set the sessions
            session['joke_num'] = new_joke_number
            session['user_pref'] = curr_user_pref
            for i in curr_user_pref:
                print(i)
            
            
            
            return render_template('recommended_jokes.html', joke= "recommended joke"+str(curr_user_pref))

        else :
            
            #for that we will set a user_pref
            user_pref = [0]*100 #create a list with the lenght of the number of jokes
            user_pref[last_joke] = value
            session['user_pref'] = user_pref
            
            #fetch the data
            #create the matrix
            #append the user_pref
            #calculate svd using the user_pref
            #that is how you get the 
            
            new_joke = 'new joke'
            new_joke_number = random.randint(1,90)#needs to be the one that is being recommend_joke
            
            #set the sessions
            session['joke_num'] = new_joke_number
             #[0,0,0,0,0,0,0,5,00,0,0,0,]
            
            #store in session
            return render_template('recommended_jokes.html', joke= "new - joke -"+str(user_pref))

class Test(db.Model):

    """Create a data model for the database to be set up for capturing user input

    """
    __tablename__ = 'Test'

    id = Column(Integer, primary_key=True)
    joke = Column(Integer, unique=False)
    
    def __repr__(self):
        userrating_repr = "<UserRating(id='%i', user_id='%i', joke_id='%i', rating = '%i')>"
        return userrating_repr % (self.id, self.user_id, self.joke_id, self.rating)


db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    debug = True