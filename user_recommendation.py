from collaborative_filter import pearson_correlation
from math import sqrt
from recommendation_data import dataset

def user_recommendation(person):
	total={}
	simSum={}
	rankings=[]

	for other in dataset:
		if other == person:
			continue

		sim = pearson_correlation(person,other)

		if sim < 0:
			continue

		for item in dataset[other]:
			if item not in dataset[person] or dataset[other][item] ==0:
				total.setdefault(item,0)
				total[item] += dataset[other][item]*sim
				simSum.setdefault(item,0)
				simSum[item] += sim

	rankings = [(total[item]/simSum[item],item) for item in total]
	rankings.sort()
	rankings.reverse()

	print total
	print simSum
	print rankings

	return [recommend_item for score,recommend_item in rankings]

print user_recommendation('Toby')