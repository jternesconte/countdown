import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    sec = x % 60
    min = int(x / 60) % 60
    hour = int(x/3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("TIME'S UP!")
