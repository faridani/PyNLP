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
	"""
	
	output = []
	for item in tokenizeString(inputString):
		if not (isStopWord(item)):
			output.append(item)
	return output
			
		

