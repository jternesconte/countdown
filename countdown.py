import time

tempo = int(input("Enter the time in seconds: "))

for x in range(tempo, 0, -1):
    seg = x % 60
    min = int(x / 60) % 60
    hora = int(x/3600)
    print(f"{hora:02}:{min:02}:{seg:02}")
    time.sleep(1)

print("TIME'S UP!")
