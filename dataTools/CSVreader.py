#
# TODO
# See: http://docs.python.org/library/csv.html

import csv
spamReader = csv.reader(open('eggs.csv'), delimiter=' ', quotechar='|')
for row in spamReader:
     print ', '.join(row)
