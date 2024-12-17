# Format specifiers = {value : flags} format a value based on what flags are inserted 
# .(number)f = round to that many decimal places(fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price = 3.456
print(f"price is ${price:.3f}")
print(f"price is ${price:.2f}")
print(f"price is ${price:.1f}")
print(f"price is ${price:.10f}")
print(f"price is ${price:010}")
print(f"price is ${price:<10}")
print(f"price is ${price:>10}")
print(f"price is ${price:^10}")
print(f"price is ${price:+}")
print(f"price is ${price: }")
price1 = 3000.456
print(f"price is ${price1:,}")
print(f"price is ${price1:,.2f}")
print(f"price is ${price1:+,.2f}")

o/p:
price is $3.456
price is $3.46
price is $3.5
price is $3.4560000000
price is $000003.456
price is $3.456     
price is $     3.456
price is $  3.456   
price is $+3.456
price is $ 3.456
price is $3,000.456
price is $3,000.46
price is $+3,000.46