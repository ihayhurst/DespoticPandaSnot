#!/usr/bin/env python3
#from pylab import plotfile, show, gca
#import matplotlib.cbook as cbook
import csv
import matplotlib.pyplot as plt

with open('multitemplog.txt', 'rb') as fname:
 #   reader = csv.reader(f)
 #   for row in reader:
 #       print row
#fname = cbook.get_sample_data('msft.csv', asfileobj=False)
#fname2 = cbook.get_sample_data('data_x_x2_x3.csv', asfileobj=False)

# test 1; use ints
#plotfile(fname, (0,5,6))

# test 2; use names
	im=plt.imshow(fname, ('date', 'volume', 'adj_close'))


	plt.show()
