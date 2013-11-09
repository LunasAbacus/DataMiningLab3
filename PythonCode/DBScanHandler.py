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
	dbscan = DB(1,0.5,'Jaccard')

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
				dbscan.CleanUpOutliers()

	print("\n"+str(dbscan.ReturnClusters()))
	print("\n\nDONE!")

if __name__ == '__main__':
    main()
