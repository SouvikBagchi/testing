import pandas as pd
import numpy as np
import sklearn
import pickle
import matplotlib.pyplot as plt
from scipy.sparse.linalg import svds
from sklearn.model_selection import train_test_split
from scipy.stats import rankdata

class Recommender:


	data_final = None
	data_joke = None
	def __init__(self, data_final, data_joke):

		self.data_final = data_final
		self.data_jokes = data_joke

	def get_most_popular(self):
	    popular_rated = self.data_final[self.data_final['Rating'] == 10]
	    popular_jokes = popular_rated.groupby('JokeID').count().reset_index()
	    popular_jokes = popular_jokes[['JokeID','Rating']]
	    popular_jokes.columns = ['JokeID','Number_rated10']
	    top_joke = popular_jokes.sort_values(by=['Number_rated10']).head(1)
	    top_joke_val = top_joke['JokeID'].values[0]
	    top_joke_desc = self.data_jokes[self.data_jokes['JokeID'] == top_joke_val].values[0][1]

	    return top_joke_desc, top_joke_val
