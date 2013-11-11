#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     08/11/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from DBSCAN2 import dbScanner as DB
import time

def main():
	# get articles in format
	# number - Title|keyword1:keyword2

	#create DBSCAN
	# TODO - handle iterative clustering for old points
	# Solution? Add all points in first, then iterate through while clustering

	#Alt solution?
	#http://scikit-learn.org/stable/modules/clustering.html

	dbscan = DB(80,0.85,'Jaccard')
	#dbscan = DB(5,0.90,'bla')

	with open('DBSCAN-large.txt','r') as f:
		#take apart line
		for line in f:
			if (len(line) > 1):
				line = line[:-1]
				parts = line.split("|")
				title = parts[0]
				wordSet = parts[1].split(":")
				#print(title+"\n")
				#print(title + str(wordSet))
				#print("\n\n")
				if (len(wordSet) > 2):
					dbscan.AddArticle(title, wordSet)

	limDist = 0.85
	minClust = 80
	while (limDist <= 0.99):
		while(minClust <= 80):
			print("\nStarted Clustering all points...["+str(limDist)+":"+str(minClust)+"]")
			dbscan.SetParameters(minClust,limDist)
			startTime = time.time()
			dbscan.ClusterAllPoints()
			endTime = time.time()

			print("Time elapsed = " + str(endTime - startTime) + " seconds")

		    #print("\n"+str(dbscan.ReturnClusters()))

			dic = {}
			dic = dbscan.ReturnClusters()

			uniqueCluster = 0

			for cluster in dic.keys():
				if (len(dic[cluster])>1):
					uniqueCluster += 1
					#print (str(cluster)+" : "+str(len(dic[cluster])))
			print (str(uniqueCluster) + " clusters")
			minClust += 10
		limDist += 0.4
		minClust = 100

	print("\n\nDONE!")


if __name__ == '__main__':
    main()
