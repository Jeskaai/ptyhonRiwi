#Level 4

fruits = ["apple", "orange", "banana", "strawberry", "grape", "mango"]
print(f"My fruit list is: {fruits} ")


print(f"The first fruit in the list is: {fruits[0]}")
print(f"The third fruit in the list is: {fruits[2]}")

fruits.append("watermelon")
print(fruits)


#B

num =  [7,23,9,2,6,9,11]

sum_total = sum(num)

quantityOfElements = len(num)

average = sum_total / quantityOfElements

print(f"The list is: {num} the total sum: {sum_total} number of elements: {quantityOfElements} \n. The average is: {average} ")


#C

num1 = [7,3,2,14,9,13,21]

pars = []


for i in num1:
    if  i % 2 == 0:
        pars.append(i)
print(f"List original: {num1}")
print(f"List numbers pars: {pars}")


#D

k = [1, 5, 2, 3, 5, 1, 4, 2, 3]

print(f"The list original: {k}")

numbers_unicos = list(set(k))

print(f"The final list: {numbers_unicos}")