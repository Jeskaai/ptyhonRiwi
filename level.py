##LEVEL 2
import operation
#A

age = int(input("Enter your age: "))
print(f"Are you of legal age " if age >= 18 else "Your are underage")

#B

num1 = float(input("Enter your number: "))

result = "Positive" if num1 > 0 else "Negative" if num1 < 0 else "Zero"

print(f"The result is {result}")

#C

num2 = int(input("Enter your number: "))
print(f"The number {num2}: Par " if num2 % 2 == 0 else "The number is impar")

#D

print("=========Basic calculator===========")

n1 = int(input("Enter your number: "))
n2 = int(input("Enter another number: "))

print("\n¿What operation do you wish to perform")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divisionn")

option = input("select an option (1/4): ")

if option == "1":
  ressl = operation.addi(n1,n2)
elif option == "2":
  ressl = operation.subt(n1,n2)
elif option == "3":
  ressl = operation.multi(n1,n2)
elif option == "4":
    ressl = operation.divs(n1,n2)
else:
   print("This option is not valid.  ")




