
## This script imports Matlab data files ( .mat)
# TODO: make it pythonic
#       Blend it with the rest of the code

import warnings
warnings.filterwarnings("ignore")

import scipy.io


def loadmat(matfile):
	#matfile should be without .mat	
	Yback = scipy.io.loadmat(matfile+'.mat')
	Y= Yback[matfile]
	return Y
