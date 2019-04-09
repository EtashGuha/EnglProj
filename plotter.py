import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

colors = ['orange', 'green','blue','red','yellow','grey','black','purple']

def plot(dict):
	num = 0
	for name in dict:
		x = dict[name].keys()
		y = dict[name].values()
		print(type(y))
		filteredy = savgol_filter(np.array(list(y)), 55, 11)
		plt.plot(x,filteredy, color = colors[num], label = "Filtered")
		num = num + 1
	plt.legend()
	plt.title("Sentiment for Each Character in Moby Dick")
	plt.ylabel("Sentiment Value")
	plt.xlabel("Line Number")
	plt.show()
