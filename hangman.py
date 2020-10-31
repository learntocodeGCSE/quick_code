import random
file = open("hangman.txt","r")
contents = file.readlines()
random = random.randint(0, len(contents)-1)

secretWord = contents[random]

if "\n" in secretWord:
    length = len(secretWord)-1

else:
    length = len(secretWord)


print(length)

guessList = ["_"]*length

counter = 0
wrong = 0

while "_" in guessList:
    if wrong > 10:
        print("You have run out of goes!")
        print("the secret word was.....", secretWord)
        print("GAME OVER")
        exit()
    print(guessList)
    guess = input("Type a letter: ").upper()

    if guess in secretWord:
        print ("Thats right!")
        counter = counter + 1

        for x in range (0, length):
            
            if secretWord[x] == guess:
                guessList[x] = guess

    else:
        print("Letter not found!")
        counter = counter + 1
        wrong = wrong + 1
    
print("You got it right! That took you", counter, "attempts")

