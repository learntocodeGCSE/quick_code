#for x in range (0,100):

 #   if x % 5 == 0 and x % 3 == 0:
  #      print("Fizz Buzz")

   # elif x % 5 == 0:
    #    print ("Buzz")

    #elif x % 3 == 0:
     #   print ("Fizz")

    #else:
     #   print(x)

for x in range (0,100):
    output = ""

    if x % 3 == 0:
        output = "Fizz"

    if x % 5 == 0:
        output = output + "Buzz"

    if output == "":
        output = x

    print(output)
