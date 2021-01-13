#Noughts and Crosses

def main():
    grid = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

    player1 = "X"
    player2 = "O"
    
    gameOver = False
    while gameOver == False:
        #player 1
        
        printGrid(grid[0],grid[1],grid[2])
        grid = turn(player1, grid)
        gameOver = winCheck(player1,grid,gameOver)

        if gameOver == False:
            #player 2
            
            printGrid(grid[0],grid[1],grid[2])
            grid = turn(player2, grid)
            gameOver = winCheck(player2,grid,gameOver)

    #Game Over

    printGrid(grid[0],grid[1],grid[2])

    print("Play Again?")
    choice = input("1. Play Again\n2. EXIT\n")

    while choice != "1" and choice != "2":
        print("Only press 1 or 2")
        print("Play Again?")
        choice = input("1. Play Again\n2. EXIT\n")

    if choice == "1":
        main()

    else:
        exit()
        

def printGrid(r1,r2,r3):
    print(r1[0],"|",r1[1],"|",r1[2])
    print("----------")
    print(r2[0],"|",r2[1],"|",r2[2])
    print("----------")
    print(r3[0],"|",r3[1],"|",r3[2])


def turn(player, grid):

    choice = 0
    while choice != " ":
        print(player, "player turn...")
        row = input("choose a row: \n1. Top \n2. Middle \n3. Bottom\n")
        while row != "1" and row != "2" and row != "3":
            print("only type 1, 2 or 3")
            row = input("choose a row: \n1. Top \n2.Middle \n3.Bottom\n")

        column = input("choose a column: \n1. Left \n2. Middle \n3. Right\n")
        while column != "1" and column != "2" and column != "3":
            print("only type 1, 2 or 3")
            column = input("choose a column: \n1. Left \n2. Middle \n3. Right\n")

        choice = grid[int(row)-1][int(column)-1]

        if choice != " ":
            print("There is already a value in that part of the grid..try again!")

        else:
            print("Updating grid...")
            grid[int(row)-1][int(column)-1] = player
            return grid

def winCheck(player,grid,gameOver):

    
#check rows:
    
    #top row
    if grid[0][0] == player and grid[0][1] == player and grid[0][2] == player:
        print("Top Row win. ",player,"Wins!")
        gameOver = True

    #middle row
    elif grid[1][0] == player and grid[1][1] == player and grid[1][2] == player:
        print("Middle Row win. ",player,"Wins!")
        gameOver = True

    #bottom row
    elif grid[2][0] == player and grid[2][1] == player and grid[2][2] == player:
        print("Bottom Row win. ",player,"Wins!")
        gameOver = True


#check columns

    #left column
    elif grid[0][0] == player and grid[1][0] == player and grid[2][0] == player:
        print("Left Column win. ",player,"Wins!")
        gameOver = True

    #middle column
    elif grid[0][1] == player and grid[1][1] == player and grid[2][1] == player:
        print("Middle Column win. ",player,"Wins!")
        gameOver = True

    #middle column
    elif grid[0][2] == player and grid[1][2] == player and grid[2][2] == player:
        print("Right Column win. ",player,"Wins!")
        gameOver = True

#Check diagonals

    elif grid [0][0] == player and grid[1][1] == player and grid[2][2] == player:
        print("Diagonal win. ", player,"Wins!")
        gameOver = True

    elif grid [0][2] == player and grid[1][1] == player and grid[2][0] == player:
        print("Diagonal win. ", player,"Wins!")
        gameOver = True

    else:
        print("No winner yet...")
    
#check for draw:

    spacesRemain = False
    
    for x in range(0,len(grid)):
        if " " in grid[x]:
            spacesRemain = True

    if spacesRemain == False:
        if gameOver == False:
            print("Its a Draw!")
            gameOver = True

    return gameOver



main()
