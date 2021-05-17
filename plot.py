from matplotlib import pyplot as plt
import numpy as np

import json

data= json.load(open('data.json', 'r'))

counted = {}

for x in data:
    if str(x) in counted:
        counted[str(x)] += 1
    else: 
        counted[str(x)] = 1


xList = []
yList = []

for key in sorted(counted.keys(), key=int) :
    print(key , " :: " , counted[key])
    xList.append(key)
    yList.append(counted[key])

plt.bar(xList,yList)

plt.show()







