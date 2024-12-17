# indexing = accessing elements of a sequence using [] (indexing operator)
# [start:end:step]

creditcard_number ='1234-4567-1345-1234'

print(creditcard_number[0])

# o/p:butulparveen@Butuls-MacBook-Pro Python % python3 string_indexing.py
# 1
print(creditcard_number[0:4])
print(creditcard_number[:4])
print(creditcard_number[5:9])
print(creditcard_number[5:])
# from last to first digit negative
print(creditcard_number[-1])
print(creditcard_number[-5])
# count every second character
print(creditcard_number[::2])
print(creditcard_number[::3])

last_digits = creditcard_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

# reverse a string :credit number backwards
creditcard_number= creditcard_number[::-1]
print(creditcard_number)


# o/p:1
# 1234
# 1234
# 4567
# 4567-1345-1234
# 4
# -
# 13-5714-24
# 145-414
# xxxx-xxxx-xxxx-1234
# 4321-5431-7654-4321