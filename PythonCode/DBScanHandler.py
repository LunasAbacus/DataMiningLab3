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

from DBSCAN import dbScanner as DB

def main():
	# get articles in format
	# number - Title|keyword1:keyword2

	#create DBSCAN
	# TODO - handle iterative clustering for old points
	# Solution? Add all points in first, then iterate through while clustering
	dbscan = DB(2,0.95,'Jaccard') #higher threshold => less similarity

	with open('output-FeatureVectorDBScan.txt','r') as f:
		#take apart line
		for line in f:
			if (len(line) > 1):
				parts = line.split("|")
				title = parts[0]
				wordSet = parts[1].split(":")
				#print(title+"\n")
				#print(title + str(wordSet))
				#print("\n\n")
				dbscan.AddArticle(title, wordSet)

	dbscan.ClusterAllPoints()

	print("\n"+str(dbscan.ReturnClusters()))
	print("\n\nDONE!")

if __name__ == '__main__':
    main()
