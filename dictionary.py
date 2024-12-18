# Dictionary = a collection of {key:value} pairs ordered and changeable.No duplicates eg;id:name,item:price
# Capitals and countries

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "Japan":"okyo",
            "Canada":"Ottawa"
}

print(capitals.get("India"))

if capitals.get("Japan"):
    print("Capital exists")
else:
    print("Capital Doesn't exists")

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
Capital exists

capitals.update({"USA":"SFO"})
print(capitals)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
{'USA': 'SFO', 'India': 'New Delhi', 'Japan': 'okyo', 'Canada': 'Ottawa'}


capitals.pop("USA")
capitals.popitem()
capitals.clear()
keys = capitals.keys()
print(keys)

# keys method
for key in capitals.keys():
    print(key)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
USA
India
Japan
Canada


# values method

for value in capitals.values():
    print(value)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
Washington D.C
New Delhi
okyo
Ottawa

values = capitals.values()
print(values)
# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
dict_values(['Washington D.C', 'New Delhi', 'okyo', 'Ottawa'])

keys = capitals.keys()
print(keys)

# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
dict_keys(['USA', 'India', 'Japan', 'Canada'])


# Item returns a 2D oject 
items = capitals.items()
print(items)


# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
dict_items([('USA', 'Washington D.C'), ('India', 'New Delhi'), ('Japan', 'okyo'), ('Canada', 'Ottawa')])

for key,value in capitals.items():
    print(f"{key}:{value}")
# o/p:
butulparveen@Butuls-MacBook-Pro Python % python3 dictionary.py
USA:Washington D.C
India:New Delhi
Japan:okyo
Canada:Ottawa

