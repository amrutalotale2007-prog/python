import math

while True:
    try:
        n = input("Enter number : ")
        if n.lower() == "exit":
            break
        print("Square root =", math.sqrt(float(n)))
    except ValueError:
        print("Invalid input!")
