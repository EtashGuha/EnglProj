from googlenlp import analyze
from plotter import plot
import collections
import string
import time

logfile = open("MobyDick.txt", "r") 
line_number = 0
numnames = dict()

numnames["Ishmael"] = collections.OrderedDict()
numnames["Nantucket"] = collections.OrderedDict()
numnames["Ahab"] = collections.OrderedDict()
numnames["Queequeg"] = collections.OrderedDict()
numnames["Stubb"] = collections.OrderedDict()
numnames["Starbuck"] = collections.OrderedDict()
for line in logfile:
	line_without_punc = line.translate(str.maketrans('','',string.punctuation))
	line_number = line_number + 1
	for name in numnames.keys():
		if name in line_without_punc.split():
			numnames[name][line_number] = analyze(line)
			time.sleep(.01)
print(numnames)
plot(numnames)
