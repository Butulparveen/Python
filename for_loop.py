# count a 10

for x in range(1,11):
    print(x)
1
2
3
4
5
6
7
8
9
10

# reverse count

for x in reversed(range(1,11)):
    print(x)

print("Happy New Year")
10
9
8
7
6
5
4
3
2
1
Happy New Year
# With 2 difference
for x in reversed(range(1,11,2)):
    print(x)
9
7
5
3
1
# With 3 difference
for x in range(1,11,3):
    print(x)

o/p:
1
4
7
10

creditcard_number = "1234-2355-1245-1245"
for x in creditcard_number:
    print(x)
o/p:
1
2
3
4
-
2
3
5
5
-
1
2
4
5
-
1
2
4
5

# How to skip a number in continuous series
for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)


o/p:1
2
3
4
5
6
7
8
9
10
11
12
14
15
16
17
18
19
20