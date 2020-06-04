#Loop exercise 6
height = int(input("height >> "))
width = int(input("width >> "))

for h in range(0, height) :
    if h == 0 or h == height -1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2)      + "*")
        