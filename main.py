import numpy as np
import operator
import math

def createDataSet():
	group = [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]
	labels = ['A','A','B','B']
	return group, labels
	
	
def classify0(inX, dataSet, labels, k):
	totalDistance = len(dataSet)*[0]
	label = {}
	labelVote = {}
	for index,dot in enumerate(dataSet):
		x = dot[0]
		y = dot[1]
		totalDistance[index] = (calculateDist(x, y, inX[0],inX[1]))
		label[totalDistance[index]] = labels[index]
		
	totalDistance = sorted(totalDistance)[ : k]
	
	for dist in totalDistance:
		if label[dist] not in labelVote:
			labelVote[label[dist]] = 0
		labelVote[label[dist]] += 1
		
	sortedClassCount = sorted(labelVote.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def calculateDist(x1, y1, x2, y2):
	return math.sqrt( math.pow(x2-x1,2) + math.pow(y2-y1,2) )



if __name__ == '__main__':
	g, l = createDataSet()
	print classify0([0,0], g, l, 3)