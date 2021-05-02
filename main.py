
import pygame
import numpy as np
from InitDraw import screen, grid, CellWidth, CellHight, Margin
from MovingOpponet import RandomMovment
from WinIdint import checkwin

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
    	running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = int(pos[0] // (CellWidth + Margin))
        row = int(pos[1] // (CellHight + Margin))
        
        # Set that location to one
        #pygame.draw.rect(screen, (255,0,0),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])
        grid[row][column] = 1
        RandomMovment(grid)
        if(checkwin(grid) != False):
          print(checkwin(grid))
          running = False
        if np.count_nonzero(grid)==9:
        	print("CAT WON")
   
  for column in range(len(grid)):
       for row in range(len(grid[column])):
           if grid[row,column] == 1:
                pygame.draw.rect(screen, (0,0,255),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])
           if grid[row,column] == 2:
                pygame.draw.rect(screen, (255,0,0),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])

  
  pygame.display.flip()



