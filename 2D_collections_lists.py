fruits = ["Apple","Orange","Banana","Pear","Pineapple"]
vegetables = ["Carrot","Beans","Chilli"]
meats = ["chicken","fish","mutton"]

groceries = [fruits,vegetables,meats]#2d list

print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][0])
print(groceries[1][2])
print(groceries[2][2])


groceries = [["Apple","Orange","Banana","Pear","Pineapple"],#2d list
["Carrot","Beans","Chilli"],
["chicken","fish","mutton"]]

print(groceries[2][0])

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 2D_collections_lists.py
['Apple', 'Orange', 'Banana', 'Pear', 'Pineapple']
['Carrot', 'Beans', 'Chilli']
['chicken', 'fish', 'mutton']
Apple
Chilli
mutton
chicken

groceries = [["Apple","Orange","Banana","Pear","Pineapple"],#2d list
["Carrot","Beans","Chilli"],
["chicken","fish","mutton"]]

for collection in groceries:
    for food in collection:
        print(food)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 2D_collections_lists.py
Apple
Orange
Banana
Pear
Pineapple
Carrot
Beans
Chilli
chicken
fish
mutton


groceries = [["Apple","Orange","Banana","Pear","Pineapple"],#2d list
["Carrot","Beans","Chilli"],
["chicken","fish","mutton"]]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 2D_collections_lists.py
Apple Orange Banana Pear Pineapple 
Carrot Beans Chilli 
chicken fish mutton 

# In 2D row can create tuples with list
groceries = [{"Apple","Orange","Banana","Pear","Pineapple"},#2d list
{"Carrot","Beans","Chilli"},
{"chicken","fish","mutton"}]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()



# 2D tuple using number pad
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 2D_collections_lists.py
1 2 3 
4 5 6 
7 8 9 
* 0 # 