# Write a program to accept marks of each subject and return total percentage

sum = 0
print('Enter marks of the following subjects.')
def prompt():
    p = input("Physics: ")
    c = input("Chemistry: ")
    m = input("Math: ")
    return p, c, m

while True:
    p, c, m = prompt()
    if p and c and m:
        if p.isdigit() and c.isdigit() and m.isdigit():
            percentage = ((int(p) + int(m) + int(c)) / 300.0) * 100
            print('Precentage is: {}%'.format(round(percentage, 2)))
            exit()

