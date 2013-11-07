import nltk
import re
import nltk.metrics.distance as Distance

from TagExtractor import ReuterRooter as RR

''' Notes:
    
'''

def main():
    reuterList = []
    filename = "reut2-000.sgm"
    print filename
    sgm = RR(filename)
    #for i in range(0, sgm.NumberOfReuters() - 1):
    for i in range(0, 20):
        title = sgm.ExtractTagData(i, "TITLE")
        title = title.lower();
        #print "title: " + str(title)
        
        topics = sgm.ExtractTagData(i, "TOPICS")
        topics = topics.lower()
        topics = re.sub("<d>", "", topics)
        topics = re.sub("</d>", " ", topics)
        topicsTokens = nltk.word_tokenize(topics)
        #print "topics: " + str(topicsTokens)
        
        body = sgm.ExtractTagData(i, "BODY")
        bodyTokens = nltk.word_tokenize(body)
        #print "body: " + str(bodyTokens)
    
        if(len(topicsTokens) != 0):
            newElement = [title, bodyTokens]
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
            #distanceMatrix[i][j] = Distance.masi_distance(set(reuterList[i][1]), set(reuterList[j][1]))
            distanceMatrix[i][j] = Distance.jaccard_distance(set(reuterList[i][1]), set(reuterList[j][1]))

    print
    print "Distance Matrix: "
    for i in range(0, len(reuterList)):
        print distanceMatrix[i]

    print "done"

    print
    print str(Distance.jaccard_distance(set(['cocoa']), set(['cocoa', 'sam'])))
              
if __name__ == '__main__':
    main()