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
		self.corePoints = []
		self.borderPoints = []
		self.noisePoints = []

		self.highestCluster = 0
		if (DistanceMetricType == 'Jaccard'):
			self.useJaccard = True;
		else:
			self.useJaccard = False;

	def PointDistance(self, point1, point2):
		if (self.useJaccard):
			return Distance.DistanceJaccard(point1.keywords, point2.keywords)
		else:
			return Distance.DistanceLevenstein(point1.keywords, point2.keywords)

	def ClassifyCluster(self, point):
		#count the number of points in vicinity
		pointCount = 0
		for dataPoint in self.data:
			if (self.PointDistance(point, dataPoint) < self.threshold):
				pointCount += 1

		if (pointCount >= self.min):
			self.corePoints.append(point)
		else:
			#check if point in neighborhood is core point
			for corePoint in self.corePoints:
				if(self.PointDistance(corePoint, point)<
				self.threshold):
					self.borderPoints.append(point)
					return
			self.noisePoints.append(point)

	def SetParameters(self,MinGroupSize, DistanceThreshold):
		self.min = MinGroupSize
		self.threshold = DistanceThreshold

	def AddArticle(self, ArticleName, ArticleTerms):
		# take only the top x terms from ArticleTerms
		#   Article terms are a dictionary of Term:Number
		point = CP(ArticleName, ArticleTerms)
		self.data.append(point)

	def ClusterAllPoints(self):
		#determin type of point: Noise, Border, Core
		for point in self.data:
			self.ClassifyCluster(point)

		#print("# core points: " + str(len(self.corePoints)))
		#print("# bord points: " + str(len(self.borderPoints)))

		for corePoint in self.corePoints:
			if (corePoint.cluster == 0):
				self.highestCluster += 1
				corePoint.cluster = self.highestCluster
			for borderPoint in self.borderPoints:
				if (borderPoint.cluster==0 and
				self.PointDistance(borderPoint,corePoint)<
				self.threshold):
					#print("Clustered core point and border point")
					borderPoint.cluster = self.highestCluster
     		for otherCorePoint in self.corePoints:
				if (otherCorePoint.cluster==0 and
				self.PointDistance(otherCorePoint,corePoint)<
				self.threshold):
					#print("Clustered two core points")
					otherCorePoint.cluster = self.highestCluster


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