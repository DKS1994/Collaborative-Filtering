from recommendation_data import dataset
from math import sqrt

def compute_similarity(person1,person2):

	both_viewed={}

	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1


	if len(both_viewed)==0:
	    return 0

	sum_of_euclidian_distan = []

	for item in dataset[person1]:
		if item in dataset[person2]:
			sum_of_euclidian_distan.append(pow(dataset[person1][item]-dataset[person2][item],2))

	sum_of_euclidian_distan = sum(sum_of_euclidian_distan)


	return 1/(1+sqrt(sum_of_euclidian_distan))


def pearson_correlation(person1,person2):
	both_viewed={}

	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item]=1

	number_of_ratings = len(both_viewed)

	if number_of_ratings==0:
		return 0

	Exy = sum([dataset[person1][item]*dataset[person2][item] for item in both_viewed])
	Ex = sum([dataset[person1][item] for item in both_viewed])
	Ey = sum([dataset[person2][item] for item in both_viewed])

	neumerator = Exy-(Ex*Ey/number_of_ratings)

	Ex2 = sum(([pow(dataset[person1][item],2) for item in both_viewed]))
	Ey2 = sum(([pow(dataset[person2][item] ,2)for item in both_viewed]))

	Sxx = Ex2-(pow(Ex,2)/number_of_ratings)
	Syy = Ey2 - (pow(Ey,2)/number_of_ratings)

	denominator = sqrt(Sxx*Syy)

	if denominator == 0:
		return 0

	return neumerator/denominator

pc = pearson_correlation('Lisa Rose','Gene Seymour')

print pc