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
import ClusterPoint

def init(self, MinGroupSize, DistanceThreshold, DistanceMetricType):
	self.min = MinGroupSize
	self.threshold = DistanceThreshold
	self.data = []
	self.highestCluster = 1
	if (DistanceMetricType == 'Jaccard'):
		self.useJaccard = True;
	else:
		self.useJaccard = False;

def IsNoise(self, ArticleSet):
	#count number of points within distance threshold
	numClosePoints = 0
	for point in self.data:
		if (self.useJaccard and Distance.DistanceJaccard(ArticleSet, point.keywords) <
			self.threshold):
				numClosePoints += 1
		elif (not self.useJaccard and Distance.DistanceLevenstein(ArticleSet, point.keywords) <
			self.threshold):
				numClosePoints += 1

	#if less than threshold, is noise point
	if (numClosePoints < self.min):
		return True
	else:
		return False

def ClosestPoint(self, newSet):
	closestPoint = None
	distance = 1000000

	for point in data:
		pointDistance = distance + 1
		if (self.useJaccard):
				pointDistance = Distance.DistanceJaccard(ArticleSet, point.keywords)
		elif (not self.useJaccard):
				pointDistance = Distance.DistanceLevenstein(ArticleSet, point.keywords)

		if (pointDistance < distance):
			closestPoint = point
			distance = pointDistance
	return closestPoint

def ClassifyCluster(self, point):
    #if not, assign to closest cluster within threshold
	closestPoint = self.ClosestPoint(ArticleTerms)
	if (closestPoint is not None):
		point.SetCluster(closestPoint.cluster)

	#if no cluster exist, create new cluster and assign
	else:
		point.SetCluster(self.highestCluster)
		self.highestCluster += 1

def AddArticle(self, ArticleName, ArticleTerms):
	point = ClusterPoint(ArticleName, ArticleTerms)

	#check if point is noise
	if (not self.IsNoise(ArticleTerms)):
		self.ClassifyCluster(point)

	self.data.append(point)


def CleanUpOutliers(self):
	#Mental note, handle outliers that aren't noise
	#go through all the noise points cluster outliers
	#if possible
	# Outliers are points below min neighbor points, but
	# within distance threshold of a cluster
	pass

def main():
	print ("This is an implementation of DBSCAN.")

if __name__ == '__main__':
    main()