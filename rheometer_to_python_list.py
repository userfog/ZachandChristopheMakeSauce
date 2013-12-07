import sys
import pprint
import os, os.path
import re
from collections import OrderedDict
pp = pprint.PrettyPrinter(indent=4)

sample_names =  ["Xanthan-0.05", "Xanthan-.1", "Xanthan-0.15", "Xanthan-0.2", 
			"Xanthan-0.25", "Xanthan-0.35", "Xanthan-0.4", 
			"Xanthan-0.45", "Xanthan-0.5", "Xanthan-0.55", "Xanthan-0.6", "Xanthan-0.65", "Xanthan-0.7"
			, "Xanthan-0.75", "Xanthan-0.8"]


colors = ["213,213,213,.5", "182,182,182,.5", "223,246,194,.5", "172,239,209,.5", 
			"165,255,176,.5", "175,206,223,.5", "60,244,188,.5", "242,221,108,.5", 
			"95,156,226,.5", "10,117,242,.5", "53,82,198,.5", "0,78,53,.5", "2,20,26,.5",
			"25,69,44,.5", "43,28,9,.5"]
# name: 'Agar 0.05',
# color: 'rgba(223, 21, 26, .5)',
# # data: [[14.9, 0.006894],...
# },

path_to_dir = "C:/Users/Zachary/Documents/GitHub/zachandchristophemakesauce/Christophe/2/Xanthan/"

data_list = []
data_dict = []
helper_dict = OrderedDict()
i = 0
for fn in os.listdir('./Christophe/2/Xanthan/'):
	f = open(os.path.abspath(os.path.join(path_to_dir,fn)), 'r').read()
	f = re.search(r"Pa\.s\r\r*(.*)$", f)
	f = f.group(1).strip().split('\r')
	f = [el.split('\t') for el in f]
	f = [el for el in f]
	l = []
	for el in f:
		e = el[1]
		x = e.split("E")
		length = len(x)
		if length == 0 or length == 1:
			element = [float(el[0]), float(e)]
			l.append(element)
		else:
			try :
				e = float(x[0]) * (10 ** int(x[1]))
				element = [float(el[0]), e]
				l.append(element)
			except Exception, e :
				Exception
	helper_dict = {"name" : sample_names[i], "color" : 'rgba('+colors[i]+')', "data" : l}
	data_dict.append(helper_dict)
	i += 1
	pp.pprint(i)


path = "C:/Users/Zachary/Documents/GitHub/zachandchristophemakesauce/Christophe/3/Xanthan/dict.out"
out = open(path, 'w+')
pprint.pprint(data_dict, out)
out.close()
	


	
