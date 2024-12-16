# Logical operators

#Or= one condition must be true
# And = Both the conditions must be true
# Not =inverts the condition(False or ture)

# Using OR example to schedule outdoor event.

temp = int(input("Enter the temperature : "))
# is_raining = input('Enter True or false:')
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")


# using AND sunny temp

temp = 20 
sunny = True
if temp >= 20 and sunny:
    print('It is Hot outside')
    print('It is Sunny')
elif 20>temp>0 and sunny:
    print("Warm outside")
    print("It is cloudy")

# using NOT sunny temp
temp = 25
sunny = False
if temp >= 20 and not sunny:
    print('It is Hot outside')
    print('It is Sunny')

