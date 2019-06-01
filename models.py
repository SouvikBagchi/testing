from views import db, app
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

class Test(db.Model):

    """Create a data model for the database to be set up for capturing user input

    """
    __tablename__ = 'Test'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=False)
    joke_id = Column(Integer, unique=False)
    rating = Column(Integer, unique=False)

    def __init__(self,id, user_id, joke_id, rating):
    	self.id = id
    	self.user_id = user_id
    	self.joke_id = joke_id
    	self.rating = rating
    def __repr__(self):
        userrating_repr = "<UserRating(id='%i', user_id='%i', joke_id='%i', rating = '%i')>"
        return userrating_repr % (self.id, self.user_id, self.joke_id, self.rating)

# class JokeDesc(db.Model):

#     """Create a data model for the table JokeDesc

#     """

#     __tablename__ = 'jokedesc'

#     joke_id = Column(Integer, primary_key=True)
#     joke = Column(String(1000), unique=False, nullable=False)


#     def __repr__(self):
#         jokedesc_repr = "<JokeDesc(joke_id='%i', joke='%s')>"
#         return jokedesc_repr % (self.joke_id, self.joke)
	
db.create_all()



