#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shiro_Raven
#
# Created:     05/11/2013
# Copyright:   (c) Shiro_Raven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#http://nltk.org/api/nltk.metrics.html
import nltk.metrics.distance as Distance

def DistanceJaccard(set1, set2):
	#first convert to two sets without
	#repeating elements
	setOfWords = []

	#get set of all words
	for word in set1:
		if (word not in setOfWords):
			setOfWords.append(word)
	for word in set2:
		if (word not in setOfWords):
			setOfWords.append(word)

	#now generate the individual
	dataSet1 = []
	dataSet2 = []

	for word in setOfWords:
		if (word in set1):
			dataSet1.append(True)
		else:
			dataSet1.append(False)

		if (word in set2):
			dataSet2.append(True)
		else:
			dataSet2.append(False)

	#now calculate distance
	union = 0.0

	for i in range(0,len(dataSet1)-1):
		if (dataSet1[i] == dataSet2[i]):
			union += 1

	return union/len(setOfWords)

def DistanceLevenstein(set1, set2):
	pass

def main():
	print "Perform sample distance calculations."
	#Distance.demo()
	print ("Levenstein Distance between [dreadful, funny] = " +
		str(Distance.edit_distance('dreadful', 'funny')))

if __name__ == '__main__':
    main()
