#-------------------------------------------------------------------------------
# Name:        DBSCAN
# Purpose:     School project
#
# Author:      Nathan Jacobs
#
# Created:     05/11/2013
# Licence:     You may not even look at this code.
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import DistanceMetrics as Distance

def init(self, MinGroupSize, DistanceThreshold, DistanceMetricType):
	self.min = MinGroupSize
	self.threshold = DistanceThreshold
	self.data = []
	if (DistanceMetricType == 'Jaccard'):
		self.useJaccard = True;
	else:
		self.useJaccard = False;

def IsNoise(self, ArticleSet):
	#count number of points within distance threshold

	#if less than threshold, is noise point
	pass

def ClosestPoint(self):
	pass

def ClassifyCluster(self):
	pass

def AddArticle(self, ArticleName, ArticleTerms):
	#check if point is noise

	#if not, assign to closest cluster within threshold

	#if no cluster exist, create new cluster and assign


	#Mental note, handle outliers that aren't noise
	pass

def main():
	print "This is an implementation of DBSCAN."

if __name__ == '__main__':
    main()