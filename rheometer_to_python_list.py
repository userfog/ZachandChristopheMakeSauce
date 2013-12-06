import sys
import pprint
import os, os.path
import re
pp = pprint.PrettyPrinter(indent=4)

path_to_dir = "C:/Users/Zachary/Documents/GitHub/zachandchristophemakesauce/Christophe/2/Agar/"

for fn in os.listdir('./Christophe/2/Agar/'):
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
	path = "C:/Users/Zachary/Documents/GitHub/zachandchristophemakesauce/Christophe/3/agar/" + fn
	out = open(path, 'w+')
	pprint.pprint(l, out)
	# out.write("[")
	# for el in l :
	# 	out.write("[%f," % el[0])
	# 	out.write("%f]" % el[1])
	# out.write("]")
	out.close()
	


	