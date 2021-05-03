
import pygame
import numpy as np
from InitDraw import screen, grid, CellWidth, CellHight, Margin, myfont, DrawStartingBoard
from MovingOpponet import RandomMovment
from WinIdint import checkwin
won = False

def mainGame():
  global grid
  global won
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
      	return

      elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
 
        scale = 3
        grid = np.empty(shape=(scale, scale))
        won = False
        DrawStartingBoard(screen)

      elif event.type == pygame.MOUSEBUTTONDOWN:
          # User clicks the mouse. Get the position
          pos = pygame.mouse.get_pos()
          # Change the x/y screen coordinates to grid coordinates
          column = int(pos[0] // (CellWidth + Margin))
          row = int(pos[1] // (CellHight + Margin))
          if grid[row][column] == 0 and won == False:
            # Set that location to one
            #pygame.draw.rect(screen, (255,0,0),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])
            grid[row][column] = 1
            RandomMovment(grid)
            if(checkwin(grid) != False):
              print(checkwin(grid))
              won = True
              EndGame(checkwin(grid))
             
            elif np.count_nonzero(grid)==9:
            	EndGame(0)
     
    for column in range(len(grid)):
         for row in range(len(grid[column])):
             if grid[row,column] == 1:
                  pygame.draw.rect(screen, (0,0,255),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])
             if grid[row,column] == 2:
                  pygame.draw.rect(screen, (255,0,0),[(((Margin + CellWidth) * column) + Margin),(Margin + CellHight) * row + Margin, CellWidth, CellHight])

    
    pygame.display.flip()

def EndGame(winner):
  pygame.draw.rect(screen,(255,255,255),pygame.Rect(0, 600, 600, 100))

  Players = ["CAT ","You ", "The Computer " ]
  message = str(Players[int(winner)]+"won the game!")
  textsurface = myfont.render(message, False, (0, 0, 0))
  screen.blit(textsurface,(20,600))
  textsurface = myfont.render("Press 'Space' To Play Again", False, (0, 0, 0))
  screen.blit(textsurface,(20,650))

 

mainGame()