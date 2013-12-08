import sys
import pprint
import os, os.path
import re
from collections import OrderedDict
import numpy as np
from matplotlib.pyplot import *

# from sklearn import linear_model

pp = pprint.PrettyPrinter(indent=4)

path_to_dir = "/Users/zachfogelson/Downloads/scraps/zandc/ZachandChristopheMakeSauce/Christophe/2/Xanthan/"

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

# pp.pprint(table_dict)

for el in table_dict :
    var_x, var_y = np.array(zip(*table_dict[el]))
    n = np.max(var_x.shape)
    X = np.vstack([np.ones(n), var_x]).T
    for x in var_x :
      for y in var_y :
        plot(x, y, 'o', label='Original data', markersize=10)
        xlabel('x values')
        ylabel('y values')
        xlim([0, 1])
        ylim([-1, 1])
        legend(loc=0)
    # a = np.linalg.lstsq(X, y)[0]
    # pp.pprint(a)




# t = len(temp)
# c = len(concentration)
# v = len(viscosity)
# print("Abc : " + str(abc) + "Expected : " + str(t - v))
# print("Temp :" + str(t))
# print("Con :" + str(c))
# print("Visc :" + str(v))
# x_temp = np.array(temp)
# x_concentration = np.array(concentration)
# y_viscosity = np.array(viscosity)
# nvar = 2
# one = np.ones(x_temp.shape)
# A = np.vstack((x_temp,one,x_concentration,one)).T.reshape(nvar,x_temp.shape[0],2)
# plt.plot(A, y_viscosity, 'o', label='Original data', markersize=10)
# plt.legend()
# plt.show()
# with open("out", "w+") as out:
#   pprint.pprint(A, out)
# for i,Ai in enumerate(A):
#   l = np.linalg.lstsq(Ai,y_viscosity)
#   # pp.pprint(l)
#   a = l[0]
#   print a

