#!/usr/bin/env python

#1. frequency distribution feature vector
#2. naive bayes classification

from TagExtractor import ReuterRooter as RR
import nltk
import re

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

def printFrequentNouns(body):
    tokens = nltk.word_tokenize(body)
    tagged = nltk.pos_tag(tokens)
    #tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
    #tagged = tagger.tag(tokens)
    #print tagged
    tagdict = findtags('NN', tagged)
    for tag in sorted(tagdict):
        print tagdict[tag]
    print

def getFreqDist(body):

    blackList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
                 '-', '=', '{', '}', '|', '[', ']', '\\', ']', ';', '\'', ':', '"',
                 ',', '.', '/', '<', '>', '?', 'to', 'a', 'is', 'and', 'be', 'the',
                 'of']

    commonWords = []

    featureVector = []

    body = re.sub("[\d]"," ", body)
    body = re.sub("[^\w]"," ", body)
    body = re.sub("\\b\w\w\\b", " ", body)
    body = re.sub("\\b\w\\b", " ", body)

    #create the black list words
    with open('stopwords.txt') as f:
        for line in f:
            commonWords.append(line.rstrip())

    #split up the word into tokens
    tokens = nltk.word_tokenize(body)
    #print tokens
    #print

    #create the tags
    tagged = nltk.pos_tag(tokens)
    ##entities = nltk.chunk.ne_chunk(tagged)
    #print tagged
    #print

    taggedCleaned = []
    for i in range(0, len(tagged)):
        if not tagged[i][0] in commonWords:
            taggedCleaned.append(tagged[i])

    #get the frequency distribution
    tag_fd = nltk.FreqDist(tagged)
    print tag_fd
    print

    #print [word + "/" + tag for (word, tag) in tag_fd if tag.startswith('V')]
    for (word, tag) in tag_fd:
        if(word not in commonWords):
            featureVector.append(word.lower())

    return featureVector[:5]

def bodyFeatures(body, wordFeatures):
    body_words = set(body)
    features = {}
    for i in wordFeatures:
        features['contains(%s)' % i] = i in body_words
    return features

def main():

    '''
    featureVector = []
    with open('output-FeatureVector4.txt','w') as wr:
        #for i in range(0,23):
        for i in range(0, 1):
            filename = "reut2-%s.sgm" % ("%03d" % i)
            print filename
            sgm = RR(filename)
            #print frequuent nouns
            for j in range(0, sgm.NumberOfReuters() - 1):
            #for j in range(0, 1):
                title = sgm.ExtractTagData(j, "TITLE")
                print title
                topics = sgm.ExtractTagData(j, "TOPICS")
                topics = topics.lower()
                topics = re.sub("<d>", "", topics)
                topics = re.sub("</d>", " ", topics)
                topics = topics.split()
                print topics
                featureVector = getFreqDist(sgm.ExtractTagData(j, "BODY"))
                print featureVector
                print
                wr.write("\n" + title)
                for k in range(0, len(topics)):
                    wr.write("\n" + topics[k])
                for l in range(0, len(featureVector)):
                    wr.write("\n" + featureVector[l])
                wr.write("\n")
    print 'done'
    '''
    
    #get all of the body words
    allBodyWords = []
    with open('output-FeatureVector4.txt','w') as wr:
        for ii in range(0, 1):
            filename = "reut2-001.sgm"
            print filename
            sgm = RR(filename)
            for jj in range(0, 40):
                #for jj in range(0, sgm.NumberOfReuters() - 1):
                body = sgm.ExtractTagData(jj, "BODY")
                body = re.sub("[\d]"," ", body)
                body = re.sub("[^\w]"," ", body)
                body = re.sub("\\b\w\w\\b", " ", body)
                body = re.sub("\\b\w\\b", " ", body)
            
                #get rid of stopped words
                commonWords = []
                with open('stopwords.txt') as f:
                    for line in f:
                        commonWords.append(line.rstrip())
            
                bodyTokens = nltk.word_tokenize(body)
                for kk in bodyTokens:
                    kk = kk.lower()
                    if not kk in commonWords:
                        allBodyWords.append(kk)

    print allBodyWords
    print

    #sort by freq distribution
    freqAllBodyWords = nltk.FreqDist(allBodyWords)
    print freqAllBodyWords
    print

    freqAllBodyWordsFeatures = freqAllBodyWords.keys()
    print freqAllBodyWordsFeatures
    print

    trainingSet = []
    featureVector = []
    with open('output-FeatureVector4.txt','w') as wr:
        for i in range(0, 1):
            filename = "reut2-001.sgm"
            print filename
            sgm = RR(filename)
            #for j in range(0, sgm.NumberOfReuters() - 1):
            for j in range(0, 40):
                title = sgm.ExtractTagData(j, "TITLE")
                title = title.lower();
                print title
                topics = sgm.ExtractTagData(j, "TOPICS")
                topics = topics.lower()
                topics = re.sub("<d>", "", topics)
                topics = re.sub("</d>", " ", topics)
                topics = topics.split()
                print topics
                print
                featureVector = getFreqDist(sgm.ExtractTagData(j, "BODY"))
                print featureVector
                print

                for k in topics:
                    trainingSet.append([bodyFeatures(featureVector, freqAllBodyWordsFeatures), k])
                #if(len(topics) > 0):
                #trainingSet.append([bodyFeatures(featureVector, freqAllBodyWordsFeatures), topics[0]])

    print trainingSet
    print

    classifier = nltk.NaiveBayesClassifier.train(trainingSet)

    print nltk.classify.accuracy(classifier, trainingSet)
    print

    classifier.show_most_informative_features(5)
    print

    text = "Showers continued throughout the week in \n\
        the Bahia cocoa zone, alleviating the drought since early \n\
        January and improving prospects for the coming temporao, \n\
        although normal humidity levels have not been restored, \n\
        Comissaria Smith said in its weekly review. \n\
        The dry period means the temporao will be late this year. \n\
        Arrivals for the week ended February 22 were 155,221 bags \n\
        of 60 kilos making a cumulative total for the season of 5.93 \n\
        mln against 5.81 at the same stage last year. Again it seems \n\
        that cocoa delivered earlier on consignment was included in the \n\
        arrivals figures. \n\
        Comissaria Smith said there is still some doubt as to how \n\
        much old crop cocoa is still available as harvesting has \n\
        practically come to an end. With total Bahia crop estimates \n\
        around 6.4 mln bags and sales standing at almost 6.2 mln there \n\
        are a few hundred thousand bags still in the hands of farmers, \n\
        middlemen, exporters and processors. \n\
        There are doubts as to how much of this cocoa would be fit \n\
        for export as shippers are now experiencing dificulties in \n\
        obtaining +Bahia superior+ certificates. \n\
        In view of the lower quality over recent weeks farmers have \n\
        sold a good part of their cocoa held on consignment. \n\
        Comissaria Smith said spot bean prices rose to 340 to 350 \n\
        cruzados per arroba of 15 kilos. \n\
        Bean shippers were reluctant to offer nearby shipment and \n\
        only limited sales were booked for March shipment at 1,750 to \n\
        1,780 dlrs per tonne to ports to be named. \n\
        New crop sales were also light and all to open ports with \n\
        June/July going at 1,850 and 1,880 dlrs and at 35 and 45 dlrs \n\
        under New York july, Aug/Sept at 1,870, 1,875 and 1,880 dlrs \n\
        per tonne FOB. \n\
        Routine sales of butter were made. March/April sold at \n\
        4,340, 4,345 and 4,350 dlrs. \n\
        April/May butter went at 2.27 times New York May, June/July \n\
        at 4,400 and 4,415 dlrs, Aug/Sept at 4,351 to 4,450 dlrs and at \n\
        2.27 and 2.28 times New York Sept and Oct/Dec at 4,480 dlrs and \n\
        2.27 times New York Dec, Comissaria Smith said. \n\
        Destinations were the U.S., Covertible currency areas, \n\
        Uruguay and open ports. \n\
        Cake sales were registered at 785 to 995 dlrs for \n\
        March/April, 785 dlrs for May, 753 dlrs for Aug and 0.39 times \n\
        New York Dec for Oct/Dec. \n\
        Buyers were the U.S., Argentina, Uruguay and convertible \n\
        currency areas. \n\
        Liquor sales were limited with March/April selling at 2,325 \n\
        and 2,380 dlrs, June/July at 2,375 dlrs and at 1.25 times New \n\
        York July, Aug/Sept at 2,400 dlrs and at 1.25 times New York \n\
        Sept and Oct/Dec at 1.25 times New York Dec, Comissaria Smith \n\
        said. \n\
        Total Bahia sales are currently estimated at 6.13 mln bags \n\
        against the 1986/87 crop and 1.06 mln bags against the 1987/88 \n\
        crop. \n\
        Final figures for the period to February 28 are expected to \n\
        be published by the Brazilian Cocoa Trade Commission after \n\
        carnival which ends midday on February 27. \n\
        Reuter"

    print text
    print

    featureVector = getFreqDist(text)
    print featureVector
    print

    t = classifier.classify(bodyFeatures(featureVector, freqAllBodyWordsFeatures))
    print t
    print

    text = "BankAmerica Corp is not under \n\
        pressure to act quickly on its proposed equity offering and \n\
        would do well to delay it because of the stock's recent poor \n\
        performance, banking analysts said. \n\
        Some analysts said they have recommended BankAmerica delay \n\
        its up to one-billion-dlr equity offering, which has yet to be \n\
        approved by the Securities and Exchange Commission. \n\
        BankAmerica stock fell this week, along with other banking \n\
        issues, on the news that Brazil has suspended interest payments \n\
        on a large portion of its foreign debt. \n\
        The stock traded around 12, down 1/8, this afternoon, \n\
        after falling to 11-1/2 earlier this week on the news. \n\
        Banking analysts said that with the immediate threat of the \n\
        First Interstate Bancorp &lt;I> takeover bid gone, BankAmerica is \n\
        under no pressure to sell the securities into a market that \n\
        will be nervous on bank stocks in the near term. \n\
        BankAmerica filed the offer on January 26. It was seen as \n\
        one of the major factors leading the First Interstate \n\
        withdrawing its takeover bid on February 9. \n\
        A BankAmerica spokesman said SEC approval is taking longer \n\
        than expected and market conditions must now be re-evaluated. \n\
        The circumstances at the time will determine what we do, \n\
        said Arthur Miller, BankAmerica's Vice President for Financial \n\
        Communications, when asked if BankAmerica would proceed with \n\
        the offer immediately after it receives SEC approval. \n\
        I'd put it off as long as they conceivably could, said \n\
        Lawrence Cohn, analyst with Merrill Lynch, Pierce, Fenner and \n\
        Smith. \n\
        Cohn said the longer BankAmerica waits, the longer they \n\
        have to show the market an improved financial outlook. \n\
        Although BankAmerica has yet to specify the types of \n\
        equities it would offer, most analysts believed a convertible \n\
        preferred stock would encompass at least part of it. \n\
        Such an offering at a depressed stock price would mean a \n\
        lower conversion price and more dilution to BankAmerica stock \n\
        holders, noted Daniel Williams, analyst with Sutro Group. \n\
        Several analysts said that while they believe the Brazilian \n\
        debt problem will continue to hang over the banking industry \n\
        through the quarter, the initial shock reaction is likely to \n\
        ease over the coming weeks. \n\
        Nevertheless, BankAmerica, which holds about 2.70 billion \n\
        dlrs in Brazilian loans, stands to lose 15-20 mln dlrs if the \n\
        interest rate is reduced on the debt, and as much as 200 mln \n\
        dlrs if Brazil pays no interest for a year, said Joseph \n\
        Arsenio, analyst with Birr, Wilson and Co. \n\
        He noted, however, that any potential losses would not show \n\
        up in the current quarter. \n\
        With other major banks standing to lose even more than \n\
        BankAmerica if Brazil fails to service its debt, the analysts \n\
        said they expect the debt will be restructured, similar to way \n\
        Mexico's debt was, minimizing losses to the creditor banks. \n\
        Reuter"
                        
    print text
    print
                        
    featureVector = getFreqDist(text)
    print featureVector
    print
                        
    t = classifier.classify(bodyFeatures(featureVector, freqAllBodyWordsFeatures))
    print t
    print
                        
    text = "Argentine grain board figures show \n\
        crop registrations of grains, oilseeds and their products to \n\
        February 11, in thousands of tonnes, showing those for futurE \n\
        shipments month, 1986/87 total and 1985/86 total to February \n\
        12, 1986, in brackets: \n\
        Bread wheat prev 1,655.8, Feb 872.0, March 164.6, total \n\
        2,692.4 (4,161.0). \n\
        Maize Mar 48.0, total 48.0 (nil). \n\
        Sorghum nil (nil) \n\
        Oilseed export registrations were: \n\
        Sunflowerseed total 15.0 (7.9) \n\
        Soybean May 20.0, total 20.0 (nil) \n\
        The board also detailed export registrations for \n\
        subproducts, as follows, \n\
        SUBPRODUCTS \n\
        Wheat prev 39.9, Feb 48.7, March 13.2, Apr 10.0, total \n\
        111.8 (82.7) . \n\
        Linseed prev 34.8, Feb 32.9, Mar 6.8, Apr 6.3, total 80.8 \n\
        (87.4). \n\
        Soybean prev 100.9, Feb 45.1, MAr nil, Apr nil, May 20.0, \n\
        total 166.1 (218.5). \n\
        Sunflowerseed prev 48.6, Feb 61.5, Mar 25.1, Apr 14.5, \n\
        total 149.8 (145.3). \n\
        Vegetable oil registrations were : \n\
        Sunoil prev 37.4, Feb 107.3, Mar 24.5, Apr 3.2, May nil, \n\
        Jun 10.0, total 182.4 (117.6). \n\
        Linoil prev 15.9, Feb 23.6, Mar 20.4, Apr 2.0, total 61.8, \n\
        (76.1). \n\
        Soybean oil prev 3.7, Feb 21.1, Mar nil, Apr 2.0, May 9.0, \n\
        Jun 13.0, Jul 7.0, total 55.8 (33.7).        REUTER"
    
    featureVector = getFreqDist(text)
    print featureVector
    print
    
    t = classifier.classify(bodyFeatures(featureVector, freqAllBodyWordsFeatures))
    print t
    print

    print 'done'

if __name__ == '__main__':
    main()
