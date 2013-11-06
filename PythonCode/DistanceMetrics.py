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

def main():
	print "Perform sample distance calculations."
	#Distance.demo()
	print ("Levenstein Distance between [dreadful, funny] = " +
		str(Distance.edit_distance('dreadful', 'funny')))

if __name__ == '__main__':
    main()
