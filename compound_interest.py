# compound interest calculator

# A=P(1+r/n)ˇt where A =final amount,P = initial principal balance ,r = interest rate ,t = number of time periods elapsed 

principal = 0
rate = 0
time = 0

while principal <= 0 :
    principal = float(input("Enter the principal amount:"))
    if principal <= 0:
        print("principal can't be less than or equal to zero")

while rate <= 0 :
    rate = float(input("Enter the rate of interest amount:"))
    if rate <= 0:
        print("rate can't be less than or equal to zero")

while time <= 0 :
    time = int(input("Enter the time of duration in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")

total = principal * pow((1+rate/100),time)
print(f"Balance after {time} years:${total:.2f} ")
print(principal)
print(rate)
print(time)

# o/p:
# butulparveen@Butuls-MacBook-Pro Python % python3 compund_interest.py
# Enter the principal amount:1000
# Enter the rate of interest amount10
# Enter the time of duration in years 1
# Balance after 1 years:$1100.00 
# 1000.0
# 10.0
# 1


# other way to write

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount:"))
    if principal <= 0:
        print("principal can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest amount:"))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

while True :
    time = int(input("Enter the time of duration in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principal * pow((1+rate/100),time)
print(f"Balance after {time} years:${total:.2f} ")
print(principal)
print(rate)
print(time)


o/p:
Enter the principal amount:100
Enter the rate of interest amount:10
Enter the time of duration in years: 1
Balance after 1 years:$110.00 
100.0
10.0
1