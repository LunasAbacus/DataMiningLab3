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
from ClusterPoint import ClusterPoint as CP

class dbScanner:

	def __init__(self, MinGroupSize, DistanceThreshold, DistanceMetricType):
		self.min = MinGroupSize
		self.threshold = DistanceThreshold
		self.data = []
		self.highestCluster = 1
		if (DistanceMetricType == 'Jaccard'):
			self.useJaccard = True;
		else:
			self.useJaccard = False;

	def IsNoise(self, point):
		#count number of points within distance threshold
		numClosePoints = 0
		for otherPoint in self.data:
			if (self.useJaccard and Distance.DistanceJaccard(point.keywords, otherPoint.keywords) <
				self.threshold):
					numClosePoints += 1
			elif (not self.useJaccard and Distance.DistanceLevenstein(point.keywords, otherPoint.keywords) <
				self.threshold):
					numClosePoints += 1

		#if less than threshold, is noise point
		if (numClosePoints < self.min):
			return True
		else:
			return False

	def ClosestPoint(self, newSet):
		closestPoint = None
		distance = 0

		for point in self.data:
			pointDistance = distance + 1
			if (self.useJaccard):
					pointDistance = Distance.DistanceJaccard(newSet, point.keywords)
			elif (not self.useJaccard):
					pointDistance = Distance.DistanceLevenstein(newSet, point.keywords)

			if (pointDistance > distance and pointDistance > self.threshold):
				closestPoint = point
				distance = pointDistance
		return closestPoint

	def ClassifyCluster(self, point):
	    #if not, assign to closest cluster within threshold
		closestPoint = self.ClosestPoint(point.keywords)
		if (closestPoint is not None and closestPoint.cluster is not 0):
			point.SetCluster(closestPoint.cluster)
		elif (closestPoint is not None and closestPoint.cluster is 0):
			point.SetCluster(self.highestCluster)
			#closestPoint.SetCluster(self.highestCluster)
			self.highestCluster += 1
		#if no cluster exist, create new cluster and assign
		else:
			point.SetCluster(self.highestCluster)
			self.highestCluster += 1

	def AddArticle(self, ArticleName, ArticleTerms):
		# take only the top x terms from ArticleTerms
		#   Article terms are a dictionary of Term:Number

		point = CP(ArticleName, ArticleTerms)
		self.data.append(point)

	def ClusterAllPoints(self):

		for point in self.data:
	        #check if point is noise
			if (not self.IsNoise(point)):
				self.ClassifyCluster(point)

		self.CleanUpOutliers()

	def CleanUpOutliers(self):
		# Outliers are points below min neighbor points, but
		# within distance threshold of a cluster

		for point in self.data:
			if (point.cluster is 0):
				#find nearest point within threshold
				closestPoint = self.ClosestPoint(point.keywords)
				if (closestPoint is not None):
	   				point.SetCluster(closestPoint.cluster)

	def ReturnClusters(self):
		clusters = {}

		for point in self.data:
			#print("returning:" + str(point.cluster) + " | " + point.articleName)
			if (point.cluster not in clusters):
				clusters[point.cluster] = []
			clusters[point.cluster].append(point.articleName)

			#now display a distance matrix
			#for point2 in self.data:
			#	print ("Distance between " + point.articleName + " : " + point2.articleName + "\n")
			#	print ("	= " + str(Distance.DistanceJaccard(point.keywords, point2.keywords)) + "\n\n")

		return clusters

	def DistanceMatrix(self):
		pass

def main():
	print ("This is an implementation of DBSCAN.")

if __name__ == '__main__':
    main()