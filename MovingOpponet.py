import random 
import numpy as np 
def RandomMovment(grid):
	Collum = random.randint(0,2)
	Row = random.randint(0,2)


	if np.count_nonzero(grid) != 9:
		if (grid[Collum, Row] == 1 or grid[Collum, Row] == 2):
	
			RandomMovment(grid)

		else:
		
			grid[Collum, Row] = 2

	