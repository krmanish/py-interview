# Write a program to accept two number and sign to perform action repetitively

MATH_OPT = {
    '+': 'addition',
    '-': 'subtraction',
    '*': 'multiplication',
    '/': 'division'
}

class Math(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

is_value_set = False
print('Welcome to Math World.. Enter number and the symbol to perform operation. like +/-/*//')
def prompt():
    d1 = input("Enter First Number: ")
    d2 = input("Enter second Number: ")
    sign = input("Enter Math Symbol: ")
    return d1, d2, sign


def call_subproc():
    while True:
        opt = input('Would you like to repeat(y/n)...')
        if opt.lower() not in ('n', 'y'):
            continue
        elif opt.lower() == 'n':
            return None

        m = input("Enter Math Symbol: ")
        if MATH_OPT.get(m):
            return m


while True:
    if not is_value_set:
        p, c, m = prompt()

    if p and c and m:
        method = MATH_OPT.get(m)
        if p.isdigit() and c.isdigit() and method:
            math = Math(int(p), int(c))
            result = getattr(math, method)()
            print('{} of two numbers {}, {}: {}'.format(method.title(), p, c, result))
            is_value_set = True
            m = call_subproc()
            if not m:
                exit()
        else:
            print('Oops! Wrong data. Try Again.')
    else:
        print('Empty value not allowed. Try Again.')

