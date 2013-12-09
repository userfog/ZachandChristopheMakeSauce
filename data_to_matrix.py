import sys
import pprint
import os, os.path
import re
from collections import OrderedDict
import numpy as np
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
# from sklearn import linear_model

pp = pprint.PrettyPrinter(indent=4)

path_to_dir = "/home/j33/zandc/ZachandChristopheMakeSauce/Christophe/2/Xanthan/"

# temp = []
# concentration = []
# viscosity = []

table_dict = dict()
i = 0
for fn in os.listdir('./Christophe/2/Xanthan/'):
  f = open(os.path.abspath(os.path.join(path_to_dir,fn)), 'r').read()
  f = re.search(r"Pa\.s\r\r*(.*)$", f)
  f = f.group(1).strip().split('\r')
  f = [el.split('\t') for el in f]
  f = [el for el in f]
  r = re.search(r"0p(\d+)", fn).group(0).split("p")
  r = float(r[0] + "." + r[1])
  abc = 1
  for el in f:
    x = float("%.2f" % float(el[0]))
    # temp.append(x)
    # concentration.append(r)
    e = el[1]
    y = e.split("E")
    length = len(y)
    if length == 0 or length == 1:
      element = float(e)
      # viscosity.append(element)
      try :
        table_dict[x].append([r,element])
      except :
        updater = {x : [[r,element]]}
        table_dict.update(updater)
    else:
      try :
        f = float(y[0]) * (10 ** int(y[1]))
        element = float(f)
        # viscosity.append(element)
        try :
          table_dict[x].append([r,element])
        except :
          updater = {x : [[r,element]]}
          table_dict.update(updater)
      except Exception, e:
        raise Exception("Hello")

# # pp.pprint(table_dict)
# new_dict = {}

# for el in table_dict :
#   y, x = np.array(zip(*table_dict[el]))
#   n = np.max(x.shape)
#   X = np.vstack([np.ones(len(x)), x]).T
#   c, m = np.linalg.lstsq(X, y)[0]
#   updater = {el : {"Slope" : m, "Const": c}}
#   new_dict.update(updater)
    # Plot the data along with the fitted line:
    # plt.plot(x, y, 'o', label='Original data', markersize=7)
    # plt.plot(x, m*x + c, 'r', label=(("%.3f" % m) + "*x + " + ("%.3f" % c)))
    # plt.grid("on")
    # plt.xlabel("Viscosity (Pa.s)")
    # plt.ylabel("Concentration (% Volume)")
    # plt.title("Guar: Linear Regression Concentration on Viscosity at " + str(el) + "c")
    # plt.legend(loc=0)
    # plt.show()
    # break
with open("./Christophe/3/Xanthan/Xanthan_plots.out", "w+") as plots:
  pprint.pprint(table_dict, plots)