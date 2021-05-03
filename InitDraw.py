import pygame
import numpy as np
pygame.font.init() 
myfont = pygame.font.Font('PressStart2P-Regular.ttf', 20)
Swidth, SHight = (600,700)
screen = pygame.display.set_mode((Swidth, SHight))

CellWidth = (600-100)/3
CellHight = (600-100)/3
Margin = 25
#create Screen

#fill Background color black
screen.fill((255,255,255))
#name window
pygame.display.set_caption('TicTacStar')

# Create an empty list for storing board
def DrawStartingBoard(screen):
	global grid
	scale = 3
	grid = np.empty(shape=(scale, scale))

	for x in range(scale):
	    for y in range(scale):
	        grid[x,y] = 0 # replace with whatever dynamically assigned value you want there    



	for row in range(3):
	        for column in range(3):
	           
	            pygame.draw.rect(screen,
	                             (0,0,0),
	                             [(Margin + CellWidth) * column + Margin,
	                              (Margin + CellHight) * row + Margin,
	                              CellWidth,
	                              CellHight])
	
DrawStartingBoard(screen)
