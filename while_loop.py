# while loop = execute some code while some condition remains true

# name = input("Enter your name :")

# while name == "":
#     print("you did not enter your name")
#     # If we not declare a condition name inside a while loop it will run infinite loop
#     name = input("Enter your name :")

# print(f"Hello {name}")
# o/p:Enter your name :Butul
# Hello Butul



# age = int(input('Enter your age:'))
# while age<0:
#     print("age can't be negative")
#     age = int(input('Enter your age:'))

# print(f"you are {age} years old")



# Food you like using while loop and not operator logical
# food = input('Enter a food you like(q to quit):')
# while not food == "q":
#     print(f"you like {food}")
#     food = input('Enter another food you like (q to quit):')
# print("bye")

# o/p:
# butulparveen@Butuls-MacBook-Pro Python % python3 while_loop.py
# Enter a food you like(q to quit):pizza
# you like pizza
# Enter another food you like (q to quit):bun
# you like bun
# Enter another food you like (q to quit):q
# bye

# Logical operator to while loop
num = int(input('Enter a number between 1-10 :'))
while num < 1 or num > 10:
    print(f"{num} is not a valid ")
    num = int(input('Enter a # between 1-10:'))

print(f'your number is {num}')

o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 while_loop.py
Enter a number between 1-10 :0
0 is not a valid 
Enter a # between 1-10:-1
-1 is not a valid 
Enter a # between 1-10:100
100 is not a valid 
Enter a # between 1-10:4
your number is 4