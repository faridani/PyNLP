def test_detectCPUs():
	import sys

	try: 
		sys.path.append("/home/siamak/Desktop/PyNLP/")
	except: 
		print "modify your sys.path.append in test-cpuInfo.py"
		
		
	from multicore.cpuInfo import detectCPUs

	print "Numer of cores: ", detectCPUs()

