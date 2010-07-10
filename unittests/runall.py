

print "Testing Multicore Package"
print "_________________________"
from test_multicore.test_cpuInfo import test_detectCPUs
test_detectCPUs()

print "\n\n\n\n\n\n\n"
print "Testing Preprocess Package"
print "_________________________"
from test_preprocess.test_tokenizeString import test_tokenizeString
test_tokenizeString()


print "\n\n\n\n\n\n\n"
print "End of tests"
print "_________________________"
