
import numpy as np
import pandas as pd
import random
import pymysql
from flask import Flask, url_for, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from settings import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from recommender import Recommender
from bototest import Boto

app = Flask(__name__)
app.secret_key = 'verysecretsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


########## DATA MODELS
class UserRating(db.Model):

    """Create a data model for the database to be set up for capturing user input

    """

    __tablename__ = 'userrating'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=False)
    joke_id = Column(Integer, unique=False)
    rating = Column(Integer, unique=False)

    def __repr__(self):
        userrating_repr = "<UserRating(id='%i', user_id='%i', joke_id='%i', rating = '%i')>"
        return userrating_repr % (self.id, self.user_id, self.joke_id, self.rating)


class JokeDesc(db.Model):

    """Create a data model for the table JokeDesc

    """

    __tablename__ = 'jokedesc'

    joke_id = Column(Integer, primary_key=True)
    joke = Column(String(1000), unique=False, nullable=False)


    def __repr__(self):
        jokedesc_repr = "<JokeDesc(joke_id='%i', joke='%s')>"
        return jokedesc_repr % (self.joke_id, self.joke)


db.create_all()


################ ROUTES

@app.route('/', methods = ['GET','POST'])
def hello_world():
    


    #query the db to check if data is present 
    #if present then don't do anything
    #else get data from s3 boto to put into rds
    data = User.query.all()
    # db.session.query()
    if data:
        print('data is present')
    else:
        print('data not present')
        
        # #add to db and print
        a = User(username = 'asdfa',email ='asdfsa@sdfs.com')
        db.session.add(a)
        db.session.flush()
        db.session.commit()

    #For direct calculation from s3
    boto = Boto()
    boto.download_rating()
    boto.download_jokes()


    #Your system now has the files - rating.csv and jokes.csv in them

    ##
    #Check if the data is already in the RDS
    #if not then get it from S3 and put it into the RDS

    
    if request.method == 'GET':
        
        return render_template('home.html')


@app.route('/jokes',methods = ['GET','POST'])
def recommend_joke():
    '''
    session - user_pref, joke_num(0-19)
    '''
    #write code to get the first joke and compute the matrix
    #we have loaded the data
    data_raw = pd.read_csv('ratings.csv' ,index_col = 0)
    data_jokes = pd.read_csv('jokes.csv', index_col = 0)
    data_final = data_raw[:100000]

    #create an object of recommender
    reco = Recommender(data_final, data_jokes)
    
    joke = reco.get_most_popular()

    
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

#################### FUNCTION FOR ADDING DATA TO RDS

def add_data():

    #first we add the ratings data
    rating = pd.read_csv('rating.csv')

    #loop through the ratings and create UserRatingObject and add to rds
    #commit at the end



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    debug = True
