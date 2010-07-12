"""
 This tweeter crawler is built on top of Django

 Todo: update the MVC model (use another MVC other than Django)
		Make it accessible and usable 
		It is not usable in this form
"""





# We setup the enviroment variable here

from django.core.management import setup_environ
import settings
import feedparser

setup_environ(settings)
 
# From now you can use ay Django elements
import time
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import nltk
from nltk.stem.porter import *
stemmer = PorterStemmer()
stopwords = nltk.corpus.stopwords.words('english')
# did not work stopwords.append("\\") #removing \ it cause MySQL problems

def remove_stopwords(text):
	content = ''
	text = nltk.word_tokenize(text)
	for w in text: 
		if w.lower() not in stopwords:
			content = content + stemmer.stem(w.lower()) + ' '
	return content
	
def remove_junk(text,wordlist):
	#removes the words that are not in the feature vector
	content = ''
	print "Text============", text
	print "wordlist ==========", wordlist
	text = nltk.word_tokenize(text)
	for w in text: 
		if w in wordlist:
			content = content + w + ' '
	print "junk removed ==========", content
	return content
def strip_ml_tags(in_text):
	"""Description: Removes all HTML/XML-like tags from the input text.
	Inputs: s --> string of text
	Outputs: text string without the tags
	
	# doctest unit testing framework

	>>> test_text = "Keep this Text <remove><me /> KEEP </remove> 123"
	>>> strip_ml_tags(test_text)
	'Keep this Text  KEEP  123'
	"""
	# convert in_text to a mutable object (e.g. list)
	s_list = list(in_text)
	i,j = 0,0
	
	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)
				
			# pops the right-angle bracket, too
			s_list.pop(i)
		else:
			i=i+1
			
	# convert the list back into text
	join_char=''
	return join_char.join(s_list)


from socialspace.v1.models import TweeterFeed, TweetsTokenized, TweetsFeaturized
Tweeps = TweeterFeed.objects.all().filter(approvedStatud=1)
print Tweeps
MyLongString = ''
for i in Tweeps:
	print i.tweeterID
	print i.id
	print '-----------'
	# Replace USERNAME with your twitter username
	url = u'http://twitter.com/'+ i.tweeterID+'?page=%s'
	
	LongStringForThisProfile = ''
	
	for x in range(3): #getting only 3 pages
		try:
			f = urlopen(url % x)
			soup = BeautifulSoup(f.read())
			f.close()
			tweets = soup.findAll('span', {'class': 'entry-content'})
			if len(tweets) == 0:
				break
			for x in tweets:
				a = strip_ml_tags(x.renderContents())
				#print  nltk.word_tokenize(remove_stopwords(a)) 
				b=unicode(remove_stopwords(a))
				print  b
				MyLongString = MyLongString + b + ' ' 
				LongStringForThisProfile = LongStringForThisProfile + b + ' '
			# being nice to twitter's servers
			time.sleep(1)
		except:
			print "urllib error gateway"
			
	try:
		ThisTokenized = TweetsTokenized.objects.get(tweeterID=i.id)
		print ThisTokenized
		ThisTokenized.featureVector = LongStringForThisProfile
		ThisTokenized.save()
		
	except:
		# making a new entry in the database
		t1=TweetsTokenized(tweeterID=i, featureVector = LongStringForThisProfile)
		print "Long string for this tweeter===========", LongStringForThisProfile
		t1.save()
		print "Making a new row"

myltext = nltk.Text(nltk.word_tokenize(MyLongString)) 	
print myltext
fdist = nltk.FreqDist(myltext)
vocabulary = fdist.keys()
#print vocabulary[:50]
#print fdist

#getting top 200 words
numberOfTopWords = 200
print "--------------------------"
print vocabulary[:numberOfTopWords]
finalFeatureWords = vocabulary[:numberOfTopWords]
print "--------------------------"

from numpy import zeros
print zeros((len(Tweeps),numberOfTopWords))

FeatureMatrix = zeros((len(Tweeps),numberOfTopWords))
mycounter=0
for i in Tweeps:
	print i.tweeterID
	print i.id
	print '-----------'
		
	ThisTokenized = TweetsTokenized.objects.get(tweeterID=i.id)
	myoutput = remove_junk(ThisTokenized.featureVector,finalFeatureWords)
	
	print " finaloutput===================", myoutput
	finaloutput = nltk.word_tokenize(myoutput)
	print "Freq Distifiesd=================", nltk.FreqDist(finaloutput)
	myFeatureVector = []
	finaloutputfreq = nltk.FreqDist(finaloutput)
	for key in finalFeatureWords:
		myFeatureVector.append(finaloutputfreq[key])
		print "Key=",key," word = ", finaloutputfreq[key]
	print "myFeatureVector==================", myFeatureVector
	print "------------------------------------------------"
	FeatureMatrix[mycounter] = myFeatureVector
	mycounter = mycounter+1
	try:
		ThisFeaturized = TweetsFeaturized.objects.get(tweeterID=i.id)
		ThisFeaturized.featureVector = myFeatureVector
		ThisFeaturized.save()
		
	except:
		# making a new entry in the database
		t1=TweetsFeaturized(tweeterID=i, featureVector = myFeatureVector)
		t1.save()
		print "Making a new row"
	
print "--------------------------------------------"
print FeatureMatrix

from pca_module import *
T, P, explained_var = PCA_svd(FeatureMatrix, standardize=True)
print "T (scores)=", T
print "--------------------------------------------"
print "P (loadings)=", P
print "--------------------------------------------"
print "explained_var (explained_var)=", explained_var
print "--------------------------------------------"
print T.shape
print P.shape

import matplotlib.pyplot as plt



fig = plt.figure(num=None, figsize=(24,18), dpi=90)
ax = fig.add_subplot(111) #,axisbg='darkslategray'
x= T[0,:]
y=T[1,:]

for i in range(0,len(Tweeps)):
	plt.annotate(Tweeps[i], (x[i],y[i]), xytext=None, bbox=dict(boxstyle="round", fc="0.8"),size=10, va="center")
	#plt.annotate(texts[i], (x[i],y[i]), xytext=None, bbox=dict(boxstyle="round", fc="0.8"),size=20, va="center")
	
ax.scatter(x, y, s=950, c=[1,0,0], marker='o', cmap=None, norm=None,
        vmin=None, vmax=None, alpha=0.45, linewidths=None,
        verts=None)
        

import time
import datetime
n = datetime.datetime.now()


filestring = "/home/siamak/media/archive/myfile-"+str(time.mktime(n.timetuple()))+".png"
plt.savefig(filestring) 
filestring = "/home/siamak/media/index.png"
plt.savefig(filestring) 
#plt.show()  
