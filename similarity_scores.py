from recommendation_data import dataset
from collaborative_filter import pearson_correlation
from math import sqrt

def similarity_scores(person,number_of_scores):

	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if other_person != person]

	scores.sort()
	scores.reverse()
	print scores[0:number_of_scores]

similarity_scores('Lisa Rose',3)