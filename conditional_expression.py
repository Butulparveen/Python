# Conditional expression =  one line statement for the if -else stmt(ternary operator )
# Print or assign one of two values based on a condition,X if condition else Y

num = 5
print('positive' if num>0 else 'negative')

# To check even or odd
num = 5
print('Even' if num % 2 == 0 else 'Odd')

# Max number
a = 4
b= 5
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)

# Age adult or child
age = 23
status = "adult" if age >= 18 else "child"
print(status)

# Temperature 
temp = 10
weather = "Hot" if temp>=20 else "Cold"
print(weather)


# User Role
# user_role = "admin"
user_role = "Guest"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)