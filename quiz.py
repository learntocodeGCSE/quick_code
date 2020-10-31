file = open("quiz.txt","r")
contents = file.readline()
splitLine = contents.split(",")

score = 0
counter = 0

while splitLine[0]!= "END":
    print("Here comes your question!")
    print(splitLine[0])
    print(splitLine[1])

    guess = input ("Answer: ").upper()

    while guess != splitLine[2] and guess != splitLine[3]:
        counter = counter + 1
        if counter > 3:
            print("GAME OVER!")
            print(score)
            exit()
        print ("Wrong answer!")
        guess = input ("Answer: ").upper()
        

    if guess == splitLine[2] or guess == splitLine[3]:
        print ("CORRECT")
        contents = file.readline()
        splitLine = contents.split(",")
        score = score + 1


print ("Thats all folks!")
print (score)
