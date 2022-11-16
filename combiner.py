# I used pandas python library to solve this problem
import pandas as pd
import os
import sys

colList = []
for i in range(1, len(sys.argv)):
	currArg = sys.argv[i]
	currCol = pd.read_csv(currArg).assign(filename = os.path.basename(currArg))
	colList.append(currCol)

combinedCSV = pd.concat(colList)
print(combinedCSV.to_csv(index = False))