#imports needed
import pygame
import time
import random

#Make the window
pygame.init()
dis_Width = 300
dis_Height = 300
dis = pygame.display.set_mode((dis_Width,dis_Height))
pygame.display.set_caption('SNAKE!')

#Colours
white = (255, 255, 255)
black = (0 , 0 , 0)
yellow = (255,255,102)
blue = (50, 150, 210)
green = (0, 255, 0)
red = (255, 50, 80)

#SnakeVariables
snakeSpeed = 30
snakeSize = 10

#To draw out snake
def snake (snakeSize, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, green, [x[0],x[1],snakeSize,snakeSize])

#To draw the score to the screen
def score(score):
    value = score_font.render("Your Score: "+str(score), True, blue)
    dis.blit(value, [0,0])


#setup the clock (more on this in the loop)
clock = pygame.time.Clock()

#For displaying information
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[dis_Width/4, dis_Height/4])

#The Main Game Function    
def gameLoop():
    gameOver = False
    gameClose = False

    #Starting position
    x1 = dis_Width / 2
    y1 = dis_Height / 2

    #amount each position will change
    x1_change = 0
    y1_change = 0

    #The snake list
    snakeList = []
    snakeLength = 1

    #Creates X and Y Coordinates for food to be placed
    foodx= round(random.randrange(0,dis_Width - snakeSize) / 10.0)*10.0
    foody= round(random.randrange(0,dis_Height - snakeSize) / 10.0)*10.0

    #While we have not hit gameOver...do this...
    while not gameOver:


        #Creating options to play again
        while gameClose == True:
            dis.fill(white)
            message("Play Again?? Y or N",red)
            pygame.display.update()

            #Captures the user input, loads the game again if they want another go
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        gameOver = True
                        gameClose = False

                    if event.key == pygame.K_y:
                        gameLoop()
            
        #for everything that happens in the window...
        for event in pygame.event.get():
            print (event)
        
            #Quit the game
            if event.type==pygame.QUIT:
                gameOver = True

            #Player key inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeSize
                    y1_change = 0

                
                if event.key == pygame.K_RIGHT:
                    x1_change = snakeSize
                    y1_change = 0


                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snakeSize


                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snakeSize


        #Every loop, check if you are out of bounds
        if x1 >= dis_Width or x1 < 0 or y1 >= dis_Height or y1 <0:
            gameClose = True

        #Update the snakes position
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [x1,y1,snakeSize,snakeSize])

        #Draw the food
        pygame.draw.rect(dis,red,[foodx, foody, snakeSize, snakeSize])
        

        #Keep track of the snakes head
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        
        #Each append, creates a mini list of 2 positions inside the snakeList
        #Like [x,y][x,y][x,y]
        snakeList.append(snakeHead)

        #overwrite position 0
        if len(snakeList) > snakeLength:
            del snakeList[0]


        #if the head collides with the body, game over
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        #Draw the snake 
        snake(snakeSize,snakeList)
        score(snakeLength)

        #Update the display
        pygame.display.update()

        #Check if the snake is in the same position as food
        if x1 == foodx and y1 == foody:
            foodx= round(random.randrange(0,dis_Width - snakeSize) / 10.0)*10.0
            foody= round(random.randrange(0,dis_Height - snakeSize) / 10.0)*10.0
            snakeLength += 1
                
        #how quickly the screen updates
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()




                











