import random

def drawAscii(aFileName):
    file = open(aFileName + ".txt","r")
    image = file.read()
    print(image)
    file.close()

    
image = random.randint(1,3)

drawAscii(str(image))
