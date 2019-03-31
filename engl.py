logfile = open("MobyDick.txt", "r") 
wordcount=0
my_word = "Ishmael"
numnames = dict()
numnames["Ishmael"] = 0
numnames["Nantucket"] = 0
for line in logfile:
	for name in numnames.keys():
	    if name in line.split():
	        numnames[name] = numnames[name] + 1

print numnames