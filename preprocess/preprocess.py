import re
import string

def removeStopWords(inputString):
	"""
	Removes the stop words from the input string
	"""
	
	
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

