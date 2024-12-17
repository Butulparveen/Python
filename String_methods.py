name = input('Enter your full name:')



result = len(name)
print(result)
o/p:Enter your full name:Butul parveen
13

result = name.find("u")
print(result)
o/p:Enter your full name:Butul
1

result = name.rfind("u")
print(result)
o/p:Enter your full name:Butul
3

result = name.capitalize()
print(result)
o/p:Enter your full name:butul parveen
Butul parveen

result = name.lower()
print(result)
o/p:Enter your full name:BUTUL
butul

result = name.upper()
print(result)
o/p:Enter your full name:butul
BUTUL

result = name.isdigit()
print(result)
o/p:Enter your full name:Butul
False
o/p:Enter your full name:123
True

result = name.isalpha()
print(result)
o/p:Enter your full name:Butul
True
o/p:Enter your full name:123
False


phone_number=input('Enter your mobile number #:')
result = phone_number.count("-")
print(result)
o/p:Enter your mobile number #:123-234-5678
2

result = phone_number.replace("-"," ")
print(result)
o/p:Enter your mobile number #:123-234-5432
123 234 5432

result = phone_number.replace("-","")
print(result)
o/p:Enter your mobile number #:123-234-5432
1232345432



print(help(str))



# validate user input exercise = username no more than 12 characters,
# usernames not contains any spaces,
# username must not contain any digits

username = input("Enter the username:")

if len(username) >= 12:
    print("username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain any spaces")
# elif not username.isdigit() == -1:
elif not username.isalpha():
    print("Your user name can't contain any digits ")
else:
    print(f"welcome {username}")