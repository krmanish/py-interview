# Q: Ask and print two number

def prompt():
    x = input("Enter first number")
    y = input("Enter Second number")
    return x, y

x, y = prompt()

while True:
    if x and y:
        if x.isdigit() and y.isdigit():
            print("Hello Dear, You sum of number is ", int(x) + int(y))
            exit(255)

    print('Input is wrong. Try again....\n')
    x, y = prompt()


# Write a program to accept input from the user until press x and return sum of them.
