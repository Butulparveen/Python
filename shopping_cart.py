foods =[]
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to Quit):')
    if food.lower() == "q":
        break
    else:
        price = float(input('Enter a price of {food}:$'))
        foods.append(food)
        prices.append(price)

print("------Your Cart -------")

for food in foods:
    print(food)

for price in prices:
    print(price)
    total += price
print(f"your total is: ${total}")



# o/p:

# butulparveen@Butuls-MacBook-Pro Python % python3 shopping_cart.py
# Enter a food to buy (q to Quit):pizza
# Enter a price of {food}:$50
# Enter a food to buy (q to Quit):bun
# Enter a price of {food}:$45
# Enter a food to buy (q to Quit):q
# ------Your Cart -------
# pizza
# bun
# 50.0
# 45.0
# your total is: $95.0