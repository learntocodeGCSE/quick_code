import time
import random

def rockPaperScissors():
    computerScore = 0
    score = 0
    
    inputList = ["Rock", "Paper", "Scissors"]
    goAgain = int(input("Press 1 to play again, 2 to QUIT"))
    while goAgain!= 1 and goAgain !=2:
        print("Number not allowed")
        goAgain = int(input("Press 1 to play again, 2 to QUIT"))

    while goAgain == 1:
        print("Select Rock, Paper or Scissor using 1, 2 or 3...")
        choice = int(input("1. Rock \n2. Paper \n3. Scissors \n"))
        while choice != 1 and choice != 2 and choice != 3:
            print("Number not allowed")
            print("Select Rock, Paper or Scissor using 1, 2 or 3...")
            choice = int(input("1. Rock \n2. Paper \n3. Scissors \n"))


        computerChoice = random.randint(1,3)

        print("Ready.....")
        time.sleep(0.2)
        print("Set.....")
        time.sleep(0.2)
        print("GO!!!")
        time.sleep(0.2)

        print("You chose:", inputList[choice-1])

        print("The Computer chose:", inputList[computerChoice-1])

        #Draw

        if computerChoice == choice:
            print("Its a DRAW!")

        else:
            #Rock
            if computerChoice == 1 and choice == 3:
                print("Computer Wins!")
                computerScore = computerScore + 1

            elif computerChoice == 3 and choice == 1:
                print("You Win!")
                score = score + 1

            #Paper
            elif computerChoice == 2 and choice == 1:
                print("Computer Wins!")
                computerScore = computerScore + 1

            elif computerChoice == 1 and choice == 2:
                print("You Win!")
                score = score + 1

            #Scissors
            elif computerChoice == 3 and choice == 2:
                print("Computer Wins!")
                computerScore = computerScore + 1

            elif computerChoice == 2 and choice == 3:
                print("You Win!")
                score = score + 1

            else:
                print("LOGIC ERROR")
                
        print("")
        print("Current Scores:")
        print("Computer:", computerScore)
        print("User:", score)
        print("")

        goAgain = int(input("Press 1 to go again, 2 to QUIT\n"))

        while goAgain !=1 and goAgain != 2:
            print("Number not allowed")
            goAgain = int(input("Press 1 to go again, 2 to QUIT\n"))
                      

rockPaperScissors()










                
                    
            
                  
