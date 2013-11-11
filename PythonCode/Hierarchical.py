import nltk
import re
import nltk.metrics.distance as Distance

import scipy
import pylab

from scipy.cluster.hierarchy import linkage, dendrogram
from TagExtractor import ReuterRooter as RR

''' Notes:
    
    Hierarchial Clustering:
    scipy.cluster.hierarchy
    
'''

def cleanTokens(tokens):
    
    print tokens
    
    blackList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
                 '-', '=', '{', '}', '|', '[', ']', '\\', ']', ';', '\'', ':', '"',
                 ',', '.', '/', '<', '>', '?', 'to', 'a', 'is', 'and', 'be', 'the',
                 'of', '``', '/''/']
                 
    stopWords = []
    newBody = []

    with open('stopwords.txt') as f:
        for line in f:
            stopWords.append(line.rstrip())

    for word in tokens:
        if(word not in stopWords and word not in blackList):
            newBody.append(word)

    return newBody

def main():
    reuterList = []
    reuterNumber = 0
    for i in range(0, 21):
        filename = "reut2-%s.sgm" % ("%03d" % i)
        print filename
        sgm = RR(filename)
        for i in range(0, sgm.NumberOfReuters() - 1):
        #for i in range(0, 20):
        
            reuterNumber = reuterNumber + 1
            print "Reuter Number: " + str(reuterNumber)

            title = sgm.ExtractTagData(i, "TITLE")
            title = title.lower();
            #print "title: " + str(title)
            
            topics = sgm.ExtractTagData(i, "TOPICS")
            topics = topics.lower()
            topics = re.sub("<d>", "", topics)
            topics = re.sub("</d>", " ", topics)
            topicsTokens = nltk.word_tokenize(topics)

            #body = sgm.ExtractTagData(i, "BODY")
            #bodyTokens = nltk.word_tokenize(body)
            #bodyTokens = cleanTokens(bodyTokens)
        
            #TODO: if there is no topics perdict them
            
            #TODO: get rid of topics with 'earn '
            #if(len(topicsTokens) != 0):
            #    if(topicsTokens[0] is not 'earn ' and len(topicsTokens) > 1):
            #        if(topicsTokens[0] is not 'acq ' and len(topicsTokens) > 1):
                    #if(len(topicsTokens) != 0):
            
            if(len(topicsTokens) >= 2):
            #if(len(topicsTokens) != 0):
                newElement = [title, topics]
                reuterList.append(newElement)
            
    print
    print "Reuter List: "
    for i in range(0, len(reuterList)):
        print reuterList[i]
    
    print
    print "Number of Elements: " + str(len(reuterList))

    #create matrix
    distanceMatrix = [[0 for x in xrange(len(reuterList))] for x in xrange(len(reuterList))]
    for i in range(0, len(reuterList)):
        for j in range(0, len(reuterList)):
            distanceMatrix[i][j] = Distance.masi_distance(set(reuterList[i][1]), set(reuterList[j][1]))
            #distanceMatrix[i][j] = Distance.jaccard_distance(set(reuterList[i][1]), set(reuterList[j][1]))

    print
    print "Distance Matrix: "
    for i in range(0, len(reuterList)):
        print distanceMatrix[i]

    print "done"
        
    print "Creating Plot: "
    fig = pylab.figure()
    #y = linkage(distanceMatrix, method = 'single')
    y = linkage(distanceMatrix, method = 'complete')
    z = dendrogram(y)

    fig.show()
    print "Saving as dendrogramLab4.png"
    fig.savefig('dendrogramLab4.png')

    #print "Entropy: " + str(nltk.probability.entropy(distanceMatrix))

    print "done"
              
if __name__ == '__main__':
    main()