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

class ClusterPoint:

	def __init__(self, ArticleName, KeyWordsSet):
		self.articleName = ArticleName
		self.keywords = KeyWordsSet
		self.cluster = 0

	def SetCluster(self, clusterNum):
		self.cluster = clusterNum

def main():
	print ("Dont run this class")

if __name__ == '__main__':
    main()
