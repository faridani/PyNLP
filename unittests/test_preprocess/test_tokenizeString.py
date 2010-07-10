def test_tokenizeString():
	import sys

	try: 
		sys.path.append("/home/siamak/Desktop/PyNLP/")
	except: 
		print "modify your sys.path.append in test_tokenizeString.py"
		
		
	from preprocess.preprocess import tokenizeString

	test_var =  tokenizeString("so, instead, I threw together something from scratch. this doesn't even use NLTK, so you should just be able to drop this script (and the accompanying stopwords file, which is a custom list I use) into whatever directory you like and run with it. I tried to keep this super simple so that (hopefully) you can run it real time. ]it gives you an ordered list of most common words and frequency counts thereof; simple but effective in terms of finding the top most important words.")
	if (test_var == ['so', 'instead', 'I', 'threw', 'together', 'something', 'from', 'scratch', 'this', 'doesn', 't', 'even', 'use', 'NLTK', 'so', 'you', 'should', 'just', 'be', 'able', 'to', 'drop', 'this', 'script', 'and', 'the', 'accompanying', 'stopwords', 'file', 'which', 'is', 'a', 'custom', 'list', 'I', 'use', 'into', 'whatever', 'directory', 'you', 'like', 'and', 'run', 'with', 'it', 'I', 'tried', 'to', 'keep', 'this', 'super', 'simple', 'so', 'that', 'hopefully', 'you', 'can', 'run', 'it', 'real', 'time', 'it', 'gives', 'you', 'an', 'ordered', 'list', 'of', 'most', 'common', 'words', 'and', 'frequency', 'counts', 'thereof', 'simple', 'but', 'effective', 'in', 'terms', 'of', 'finding', 'the', 'top', 'most', 'important', 'words']):
		print "tokenizeString(inputString) works properly"


	
