print("Welcome to the sorting hat...")
print("Answer the questions to find your Hogwarts House!")

file = open("sorting hat.txt","r")
line = file.readline()
sortingHat = line.split(",")

hogwartsHouse = []

while sortingHat[0] != "END":
    print (sortingHat[0])
    print ("1: ",sortingHat[1])
    print ("2: ",sortingHat[2])
    guess = input("Type 1 or 2")

    if guess == "1":
        hogwartsHouse.append(sortingHat[3])
        line = file.readline()
        sortingHat = line.split(",")

    elif guess == "2":
        hogwartsHouse.append(sortingHat[4])
        line = file.readline()
        sortingHat = line.split(",")

    else:
        guess = input("Number not allowed, try again...")

print (hogwartsHouse)

gryffindor = hogwartsHouse.count("G")
slytherin = hogwartsHouse.count("S")
ravenclaw = hogwartsHouse.count("R")
hufflepuff = hogwartsHouse.count("H")

sortedList = sorted([(gryffindor, "G"),(slytherin, "S"),(ravenclaw, "R"),(hufflepuff,"H")], key = None, reverse = True)

print(sortedList[0])

if "G" in sortedList[0]:
    print("You are in.....GRYFFINDOR!")

if "S" in sortedList[0]:
    print("You are in....SLYTHERIN!")


if "R" in sortedList[0]:
    print("You are in....RAVENCLAW!")

if "H" in sortedList[0]:
    print("You are in....HUFFLEPUFF!")


