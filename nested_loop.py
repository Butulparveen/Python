for x in range(1,10):
    print(x,end="")
o/p:
123456789


for x in range(1,10):
    print(x,end="-")
o/p:
1-2-3-4-5-6-7-8-9

for x in range(3):
    for y in range(1,10):
        print(y,end="")
o/p:27 iterations
# 123456789123456789123456789

for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()

o/p:
123456789
123456789
123456789

# Rectangle
rows = int(input('Enter the number of rows:'))
columns = int(input('Enter the number of columns:'))
symbols = input('Enter the symbol:')

for x in range(rows):
    for y in range(columns):
        print(symbols,end="")
    print()

o/p:
Enter the number of rows:2
Enter the number of columns:3
Enter the symbol:$
$$$
$$$

# Table 
columns = int(input('Enter the tables between to digits:'))
rows = int(input('Enter the tables between to digits:'))
for x in range(1,rows+1):
    for y in range(1,columns+1):
        print(f"{x*y}",end="\t")
    print()
o/p:
Enter the tables between to digits:4
Enter the tables between to digits:4
1       2       3       4
2       4       6       8
3       6       9       12
4       8       12      16
# for one table multiplication

table = int(input('Enter the table number for multiplication:'))
for x in range(1,11):
    print(f"{table}*{x}={table*x}")

o/p:
Enter the table number for multiplication:3
3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27
3*10=30