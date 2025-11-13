# grading system

print("========QUALIFICATION========")

note = float(input("Enter your class grade (1.0 / 5.0): "))

if 1.0 <= note <= 2.9:
   print("Fail")
elif 3.0 <= note <= 3.9:
   print("Pass")
elif 4.0 <= note <= 5.0:
   print("Excellent")
else:
   print("Invalid number")


#SHOP

print("===========SHOP=============")
print("Prices are in dollars.")

price = {
    "SmartTV": 2.500,
    "SamsungA36": 450,
    "Ps5": 500,
    "AirpodsPro3": 250,
    "Iphone16": 850
}

cart = {}

def addProduct(product, quantity):
   if product not in price:
      print(f"Err: this product {product} It is not available in the store")
      return

   if product in cart:
      cart[product] += quantity
   else:
      cart[product] = quantity
   print(f"Added! {quantity} x {product} (s) to cart")

def showTotalCart():
   print("\n--- 🛒 YOUR SHOPPING CART ---")

   if not cart:
      print("Your cart is empty")
      return
   totalPurchases = 0

   for product , quantity in cart.items():
      unitPrice = price[product]
      subTotal = unitPrice * quantity

      print(f"* {product}: {quantity} u. x ${unitPrice:.2f} c/u = ${subTotal:.2f}")

      total_purchase += subTotal

      print("----------------------------")

      print(f"TOTAL TO PAY: ${total_purchase:.2f}")

 
addProduct("Tablet", 3)

showTotalCart()



#CASHIER

balanceInWallet = 500.000


print("==============CASHIER================")

while True:
   print("Please select an option: ")
   print("1. Check balance")
   print("2. deposit money")
   print("3. withdraw money")
   print("4. go out")

   option = input("Please write the option: ")

   if option == "1":
        print(f"your current balance is: ${balanceInWallet:.2f}")
   elif option == "2":
      try:
         amount = float(input("Enter the amount of money to deposit:  "))

         if amount > 0:
            balanceInWallet += amount
            print(f"Deposit successful. You have deposited: {amount:.2f}")
            print(f"Your new balance is: {amount:.2f}")
         else:
            print("Error: The amount to be deposited must be positive.")

      except:
         print("Error: Invalid entry. Please enter a number.")
   elif option == "3":
      try:
         amount = float(input("Enter the amount to withdraw: "))

         if amount <= 0:
            print("Error: The amount to withdraw must be positive.")
         elif amount > balanceInWallet:
            print("Error: Insufficient funds.")
            print(f"You only have ${balanceInWallet:.2f} available")
         else:
            balanceInWallet -= amount
            print(f"Successful withdrawal. You have withdrawn: ${amount:.2f}")
            print(f"Your new balance is: ${balanceInWallet:.2f}")
         
      except ValueError:
         print("Error: Invalid entry. Please enter a number.")
   elif option == "4":
      
      print("\n Thank you for using the ATM. Goodbye!!")
      break
   else:
      print("Invalid option. Please try again with a number from 1 to 4..")


#Little datebase

dataBase = []

idNext = 101


def searchForId (id_search):
   for student in dataBase:
      if student ["id"] == id_search:
         return student
   return None


def calculateOfAverage(notee):
   if not notee:
      return 0.0
   return sum(notee) / len(notee)

def addStudent():
   global  idNext
   print("\n ---- Add New Student ----")
   name = input("Name of student: ")
   course = input("Course of student: ")

   new_student = {
      "id": str(idNext),
      "name": name,
      "course": course,
      "notee": []
   }

   dataBase.append(new_student)

   print(f"Student '{name}' added successfully!")
   print(f"Your assigned ID is: {idNext}")

def showStudent():
   print("====List of student=====")

   if not dataBase:
      print("There are no students in our university's database..")
      return
   for est in dataBase():
      prom = calculateOfAverage(est["Notes"])
      print(f"ID: {est["Id"]} | Name: {est["name"]} | Course: {est["Course"]}")
      print(f"  Notes: {est["notes"]} | Average: {prom:.2f}")
      print("-" * 30)

def searchStudent():
   print("------ Search student ------")
   idSearch = input("Enter the student ID: ")

   student = searchStudent(idSearch)

   if student:
      print("¡Student found!")
      prom = calculateOfAverage(student["notes"])
      print(f"ID: {student['id']}")
      print(f"Name: {student['name']}")
      print(f"Course: {student['course']}")
      print(f"Notes: {student['notes']}")
      print(f"Average: {prom:.2f}")
   else:
      print(f"Error: No student was found with the ID {idSearch}.")


