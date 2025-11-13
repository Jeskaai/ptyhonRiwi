#LEVEL 3
import random
#A

print("---- Countinng from 1 to 10 -----")

for number in range(1,11):
    print(number)

#B

print("----- Sum of 1 to N -----")

n = int(input("Enter one number: "))

total = 0

for i in range(1, n + 1):
    total += 1
print(f"The sum from 1 to {n} is: {total}..")


##C

print("==============MULTIPLICATION TABLE=================")
numb4 = int(input("multiplication table let's see: "))
print(f"\n--- Table of {numb4} ---")

for i in range (1,11):
    ft =  numb4 * i
    print(f"{numb4} x {i} = {ft}")

##D

numb = int(input("Start the count from: "))

while numb >= 1:
    print(numb)

numb -= 1

## E

print("--- Guess the Number Game! ---")

number_secret = random.randint(1,100)
nnumber = 0
print("I've thought of a number between 1 and 100. Try to guess it!..")

while True:

    try:
        userAttempt = int(input("write your number: "))
        nnumber += 1

        if userAttempt < number_secret:
            print("too low try again..")
        elif userAttempt > number_secret:
            print("too loud try again..")
        else:
            print(f"Congratulations! You guessed the number. It was: {number_secret}")
            print(f"I take you {nnumber} ATTEMPTS..")
            break
    except ValueError:
        print("Error: That's not a number. Please enter only numbers.")


##F

out = 1

while out != 0:
    
    print("still inside")
    try:
         out = int(input("Enter 0 to exit: "))
    except ValueError:
        print("Error that was not a nnnumber..")
        out = 1

print("Loop Exited! ")


