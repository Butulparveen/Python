# write a prgm of a 90 display grade according to criteria a= 90>,b=80-90,c=80-60,d=below 60.

marks = float(input("Enter the marks:"))
if marks >=0 and marks <=100:
    if marks >= 90 and marks <= 100:
        print("A grade ")
    if marks >= 80 and marks < 90:
        print("B grade")
    if marks >= 60 and marks <80:
        print("C grade")
    if marks <60 and marks >=0:
        print("D Grade")
else:
    print("No Grade")

