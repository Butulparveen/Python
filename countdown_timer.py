# import time
# my_time = int(input("Enter the time in seconds:"))
# for x in range(0,my_time):
#     print(x)
#     time.sleep(1)
# print("Times up")

# o/p:
# butulparveen@Butuls-MacBook-Pro Python % python3 countdown_timer.py 
# Enter the time in seconds:4
# 0
# 1
# 2
# 3
# Times up

# Backwards
# import time
# my_time = int(input("Enter the time in seconds:"))
# for x in reversed(range(0,my_time)):
# # for x in range(my_time,0,-1):using step function
#     print(x)
#     time.sleep(1)
# print("Times up")

# o/p:
# Enter the time in seconds:3
# 2
# 1
# 0
# Times up


# Digital clock
import time
my_time = int(input("Enter the time in seconds:"))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times up")