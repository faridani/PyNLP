import re
import string

stopWords = open('stopWords.data', 'r').readlines()
newstopWords = [' ']
for word in stopWords:
	newstopWords.append(word.replace("\n",""))
	
stopWords = newstopWords 


def tokenizeString(inputString):
       """
       Tokenizes a string (splits the string into words)
       
       modified from a code by Eric Baumer 
       """

       # use a regular expression to remove punctuation and line breaks
       punct = re.compile('[%s]' % re.escape(string.punctuation))
       inputString = punct.sub(' ', inputString)
       # and remove line breaks
       inputString = inputString.replace('\n', ' ')

       # now split into words and return
       return inputString.split()



def isStopWord(inputWord):
	"""
	Returns True if the inputWord is a stopword
	"""
	if inputWord.lower() in stopWords:
		return True 
	else:
		return False
		
		
def removeStopWord(inputString):
	"""
	Removes a stop word from a sentence
	
	The input can be either a string or a list of words
	for example you can insert the output of a stemmer as an input here
	
	"""
	
	output = []
	
	if type(inputString)==type(str()):
		for item in tokenizeString(inputString):
			if not (isStopWord(item)):
				output.append(item)
	if type(inputString)==type(list()):
		for item in inputString:
			if not (isStopWord(item)):
				output.append(item)


	return output
			
		
if __name__=="__main__":
	# I write the tests here
	# TODO: move them to the test module
	
	
	print 
	print 
	
	from porterStemmer import Stem
	myText = "The Noronha skink is a species of skink from the island of Fernando de Noronha off northeastern Brazil. Perhaps seen by Amerigo Vespucci in 1503, it was first formally described in 1839. Its subsequent taxonomic history has been complex, riddled with confusion with Trachylepis maculata and other species, homonyms, and other problems. "
	print "removing stop words"
	print removeStopWord((myText))
	print 
	print removeStopWord(removeStopWord(myText))
	print 
	print "Stemming"
	print "Stem Sentence"
	print Stem(myText)
	print
	print
	print 
	print "Stem List"
	print Stem(removeStopWord(myText))
	# StemSentence(
