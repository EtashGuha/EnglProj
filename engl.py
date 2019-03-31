from googlenlp import analyze

logfile = open("MobyDick.txt", "r") 
line_number = 0
my_word = "Ishmael"
numnames = dict()
numnames["Ishmael"] = dict()
numnames["Nantucket"] = dict()
for line in logfile:
	line_number = line_number + 1
	for name in numnames.keys():
	    if name in line.split():
	    	numnames[name][line_number] = analyze(line)
print(numnames)