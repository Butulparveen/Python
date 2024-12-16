#mac shift+option+8 = °
#windows:Alt + 0176 = °

#fahrenheit = (°c*9/5)+32
#celcius = (°F-32)*5/9

unit = input('Is this temperature in celcius or fahrenheit (C/F):')
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((temp * 9)/5+32,1)
    print(f"The temperature in fahrenheit : {temp}°F")
elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"The temperature in Celcius : {temp}°C")

else:
    print(f"{unit} is not valid temperature")
