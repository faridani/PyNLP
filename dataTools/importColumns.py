"""
 This script imports columnar data files 
 TODO: make it pythonic
       Blend it with the rest of the code


 Example
	0.828947	0.664474	0.861842	0.213904	0.657754	
	0.171123	0.170856	0.000000	0.004605	0.111497	
	0.616071	0.678571	0.616071	0.687500	0.776786	
	0.151786	0.526786	0.616071	0.410714	0.750000	
	1.000000	0.237433	0.336898	0.301872	0.700535	
	0.887576	0.887273	0.662121	0.863636	0.614000	
	0.360963	0.705882	0.855615	0.887701	0.941176	
	0.000000	0.677632	0.203947	0.500000	0.013158	
	0.288770	0.727273	0.283422	0.941176	0.278075	
	0.304813	0.385027	0.673797	0.732620	0.561497	
	0.269737	0.459893	0.978610	0.646791	0.759358	

"""

def importColumnar(fileName):
   
   import os.path
   
   if (not os.path.exists(fileName)):
	   print "ERROR: incorrect path to file"
   if (not os.path.isfile(fileName)):			 # Does file exist?  Is it a file, or a directory?
	   print "ERROR: file does not exist"


   from numpy import loadtxt

   f = loadtxt(fileName)
   return f
   
if __name__=="__main__":
	f = importColumnar('testData.mat')
	print f
