#!/bin/env python
from collections import Counter
import bisect
import matplotlib.pyplot as plt
import numpy as np

char_count_f = 'char_count.txt'
x = [x*100 for x in range(10)]
def conv_int(str_input):
    try:
        f_in = float(str_input)
        i_in = int(f_in)
    except:
        i_in = int(str_input)
    return i_in

with open(char_count_f,'r') as i_file, open ('outfile','w') as o_file:
    appr_list = []
    for line in i_file:
        str_input = line.split()[1]
        appr_list.append(conv_int(str_input))

#hist = np.histogram(appr_list,bins=[0]+x)
output = Counter(x[bisect.bisect_left(x, item)] for item in appr_list)
for c in output:
    print "|{:5d} | {:5d}|".format(c,output[c])
