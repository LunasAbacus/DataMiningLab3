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

	return 1.0 - union/len(setOfWords)

def DistanceLevenstein(set1, set2):
    pass
    #totalDistance = 0
    #for word1 in set1:
    #    for word2 in set2:
    #       total += Distance.edit_distance(word1, word2)

def main():
    print "Perform sample distance calculations."
    print("MASI Distance between ['funny', 'jack'] and ['jack', 'funny'] = " +
        str(Distance.masi_distance(set(['funny', 'jack']), set(['jack', 'funny']))))
    print("MASI Distance between ['funny', 'jack', 'sarah'] and ['jack', 'funny'] = " +
        str(Distance.masi_distance(set(['funny', 'jack','sarah']), set(['jack', 'funny']))))
    print ("Levenstein Distance between [dreadful, funny] = " +
        str(Distance.edit_distance('dreadful', 'funny')))
    print ("Levenstein Distance between [funny, funny] = " +
        str(Distance.edit_distance('funny', 'funny')))
    print ("Levenstein Distance between ['jim', 'sally', 'jack'] and ['jack', 'jim', 'sally'] = " +
        str(Distance.edit_distance(['jim', 'sally', 'jack'], ['jack', 'jim', 'sally'])))
    print("Jaccard Distance between ['sally', 'jim']) and set(['jim', 'sally'] = " +
        str(Distance.jaccard_distance(set(['sally', 'jim']), set(['jim', 'sally']))))

if __name__ == '__main__':
    main()
