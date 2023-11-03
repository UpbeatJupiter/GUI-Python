product_name = "Pen"
price = 5
available = True

print(product_name + "$" + str(price) + ".")
print(f"{product_name} ${price}.")

age = input("Enter your age: ") 

age += 1
print(age) # Error to add int to string 

#instead do

age = int(input("Enter your age: "))
age += 1
print(age)

a = b = c = "Hey" #all of the variables value is the same 
d, e, f = 3, "A", False #every variable has different values
print(a, b, c) #Hey Hey Hey
print(d, e, f) #3 A False


num1 = 5
num2 = 7

if num1 > num2:
    print(f"{num1} is greater than ${num2}.")
    print("-------First condition---------")
elif num2 > num1:
    print(f"{num2} is greater than ${num1}.")
    print("-------Second condition---------")
else:
    print("Numbers are equal.")
    print("-------Third condition---------")

