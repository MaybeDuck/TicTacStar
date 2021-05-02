import numpy
import math

def checkRows(set):
	for i in range(len(set)):

		if(CheckUniqueItems(set[i])==1):
			return set[i][0]
		row = []
		for l in range(len(set[i])):
			row.append(set[l][i])
	
		if(CheckUniqueItems(row)==1):
			return row[0]
	return False
def checkDiagals(set):
	stringedGrid = []
	Revsed = []
	for i in range(len(set)):
		for l in range(len(set[i])):
			stringedGrid.append(set[i][l])
			Revsed.append(set[abs(l-(len(set)-1))][i])
	LD = []
	RD = []
	for i in range(len(stringedGrid)):
		

		if(i%4==0):
			LD.append(stringedGrid[i])
			RD.append(Revsed[i])



	if(CheckUniqueItems(LD)==1) or CheckUniqueItems(RD)==1:

			return LD[0]

	return False

def checkwin(set):
	WinningRow = checkRows(set)
	WinningDiangle = checkDiagals(set)

	if (WinningRow != False) or (WinningDiangle != False):
		if((WinningRow != False)):
			return WinningRow
		else:
			return WinningDiangle
	else:
		return False
def CheckUniqueItems(input_list, JustCount = True):
	ellemt = input_list[0]
	count = -len(input_list)+1

	for item in input_list:
	    if item != 0 and item == ellemt:

	        count += 1
	       
	if(JustCount == True):
		
		return count
	else: 
		return ellemt






