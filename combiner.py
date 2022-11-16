# I used pandas python library to solve this problem
import pandas as pd
import os
import sys

'''
Define Combiner Class which has 2 methods: 
Arg Check, Combine
'''
class Combiner:

	# check if argv has the correct number
	def argCheck(argv):
		# if not enough arg for path in input, return false
		if len(sys.argv) < 2:
			print("Please give the correct number of inputs. ")
			return False
		# transfer the rest of args into a list
		pathList = sys.argv[1:]
		# check the validity of each path
		for path in pathList:
			if not os.path.exists(path):
				print("Cannot find file " + path)
				return False
		return True

	# the combine method
	def combine(argv):
		colList = []
		# use the pd method to combine two files
		for i in range(1, len(sys.argv)):
			currArg = sys.argv[i]
			currCol = pd.read_csv(currArg).assign(filename = os.path.basename(currArg))
			colList.append(currCol)

		combinedCSV = pd.concat(colList)
		print(combinedCSV.to_csv(index = False))


'''
Initiate Main Class
'''
def main():
	csvCombiner = Combiner()
	if csvCombiner.argCheck():
		csvCombiner.combine()
	else:
		print("Error: cannot combine")

'''
Run Main Program
'''
if __name__ == '__main__':
	main()

