# Write a program to accept input from the user until press x and return sum of them.

sum = 0

def prompt():
    x = input("Enter a number: ")
    return x

while True:
    x = prompt()
    if x:
        if x.isdigit():
            sum = sum + int(x)
        elif x.lower() == 'x':
            print('Sum of number is: ', sum)
            exit(255)

