
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR
import re
import sys
import operator
import collections

def AddToDict(daDic, word, blacklist):
    if (len(word) > 2) and (word not in blacklist):
        if word in daDic:
            daDic[word] += 1
        else:
            daDic[word] = 1

def main():
	articleMap = {}
	blacklist = []

    #todo - use stop word found at
    #http://www.webconfs.com/stop-words.php
    #alread created file just read it
	with open('stopwords.txt') as f:
		for line in f:
			blacklist.append(line.rstrip())

	print ("printing first " + str(sys.argv[1]) + "sgm files")

	with open('DBScan-mid.txt','w') as wr:
		articleNumber = 1000

        #for i in range(0,23):
		try:
		    numSmgs = int(sys.argv[1])
		except ValueError:
		    print("Invalid number passes as argument")
		    numSmgs = 1
		for i in range(0,numSmgs):
			filename = "reut2-%s.sgm" % ("%03d" % i)
			print (filename)
			sgm = RR(filename)
			for j in range(0,sgm.NumberOfReuters()-1):
		    #for j in range(0,1):
				article = {}
				title = sgm.ExtractTagData(j,"TITLE")
				title = re.sub("\s", " ", title)
				#print title
				#wr.write("\n"+title)
				body = sgm.ExtractTagData(j,"BODY")
				body = re.sub("[\d]"," ", body)
				body = re.sub("[^\w]"," ", body)
				body = body.lower()
				for token in body.split():
				    #print token
					AddToDict(article, token, blacklist)
				wr.write("\n"+str(articleNumber)+"-"+title+"|")

				#sort article words by number times seen
				sorted_x = sorted(article.items(), key=operator.itemgetter(1))
				for pair in sorted_x[0:20]:
					wr.write(pair[0]+":")

				#for key in sorted(article.keys()):
				    #print key + ":" + str(article[key])
				#	wr.write(key + ":")
				if (len(article) < 1):
					wr.write("emptySet")
				articleMap[title] = article
				articleNumber += 1
		    #print articleMap
		print ('done')

if __name__ == '__main__':
    main()
