# Collection = single variable used to store multiple values
# List = [] ordered and changeable .Duplicates ok.
# Set = {} unordered and immutable, but add/remove ok.No Duplicates
# Tuple = () ordered and unchangeable.Duplicates ok. Faster


fruits = ["Apple","orange","Banana","Pear"]

print(fruits)
print(fruits[0]) #index operator
print(fruits[0:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])#Fruits backwards

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))

# Boolean in collection true or false 
print("apple" in fruits)

for fruit in fruits:
    print(fruit)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 collection.py
['Apple', 'orange', 'Banana', 'Pear']
Apple
['Apple', 'orange', 'Banana']
['Apple', 'orange', 'Banana']
['Apple', 'Banana']
['Pear', 'Banana', 'orange', 'Apple']
4
False
Apple
orange
Banana
Pear


# Lists 
to update apple with pineapple
fruits = ["Apple","orange","Banana","Pear"]
fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)
# o/p:
pineapple
orange
Banana
Pear

# To add in list using append method
fruits = ["Apple","orange","Banana","Pear"]
fruits.append("pineapple")
print(fruits)

# o/p:
['Apple', 'orange', 'Banana', 'Pear', 'pineapple']


# To remove in list using remove method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
fruits.remove("Apple")
print(fruits)

# o/p:
['orange', 'Banana', 'Pear', 'pineapple']

# To insert in list using insert method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
fruits.insert(0,"Apple")
print(fruits)


# o/p:
['Apple', 'Apple', 'orange', 'Banana', 'Pear', 'pineapple']

# To sort in list using sort method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
fruits.sort()
print(fruits)

# o/p:
['Apple', 'Banana', 'Pear', 'orange', 'pineapple']


# To reverse in list using reverse method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
fruits.reverse()
print(fruits)

# o/p:
['pineapple', 'Pear', 'Banana', 'orange', 'Apple']


# To Clear in list using clear method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
fruits.clear()
print(fruits)


# o/P
[]

# To index in list using index method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
print(fruits.index("orange"))
print(fruits)

# o/p:
1
['Apple', 'orange', 'Banana', 'Pear', 'pineapple']

# To count in list using count method
fruits = ["Apple","orange","Banana","Pear","pineapple"]
print(fruits.count("orange"))
print(fruits)

# o/p:
1
['Apple', 'orange', 'Banana', 'Pear', 'pineapple']


# Set,indexing operator are not used by set method
fruits = {"Apple","orange","Banana","Pear","orange"}
print(dir(fruits))
print(help(fruits))
fruits = {"Apple","orange","Banana","Pear","orange"}
fruits.add("pineapple")
print(fruits)
fruits.remove("pineapple")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear() #Set()
# o/p:
{'pineapple', 'Pear', 'Apple', 'orange', 'Banana'}
{'Pear', 'Apple', 'orange', 'Banana'}
{'Apple', 'orange', 'Banana'}



# Tuples-count and index,len,
fruits = ("Apple","orange","Banana","Pear","orange")
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("Apple"))
print(fruits.count("orange"))
for fruit in fruits:
    print(fruit)

# o/p:
5
False
0
2
Apple
orange
Banana
Pear
orange