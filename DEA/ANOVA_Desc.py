"""
Data Envelopment Analysis implementation

Sources:
Sherman & Zhu (2006) Service Productivity Management, Improving Service Performance using Data Envelopment Analysis (DEA) [Chapter 2]
ISBN: 978-0-387-33211-6
http://deazone.com/en/resources/tutorial

"""

import numpy as np
from scipy import stats as st

#DESCRIPTIVE STATS
csv = np.genfromtxt('results.csv', delimiter=",", dtype=None, names=True)

names = csv["NAMES"].astype('U')
dea = csv["DEA"].astype("float32")

desc = st.describe(dea)
print(desc)
print("")


#ANOVA TESTS
'''
Start with calculating the Sum of Squares between.  Sum of Squares between is variability due to interation between the groups.  Sometimes known as the Sum of Squares of the Model.
'''
csv2 = np.genfromtxt('dataset.csv', delimiter=",", dtype=None, names=True)


new = []
for row in csv2:
    name, input1, input2, input3, output1, output2, output3 = row[0].astype('U'), row[1].astype('U'), row[2].astype('U'), row[3].astype('U'), row[4].astype('U'), row[5].astype('U'), row[6].astype('U')
    new.append([float(input1), float(input2), float(input3), float(output1), float(output2), float(output3)])


results = st.f_oneway(new[0], new[1], new[2], new[3], new[4], new[5], new[6], new[7], new[8], new[9], new[10], new[11], new[12], new[13], new[14], new[15], new[16], new[17], new[18], new[19], new[20])
print(results)


