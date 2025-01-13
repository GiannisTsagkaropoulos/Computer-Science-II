import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def str_to_number(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)

class Complex():
    def __init__(self, re = 0, im = 0):
        while not(is_number(re)):
            print('Το πραγματικό μέρος του μιγαδικού πρέπει να είναι πραγματικός αριθμός.')  
            re = input('Πραγματικό μέρος: ' )
        while not(is_number(im)):    
            print('Το φανταστικό μέρος του μιγαδικού πρέπει να είναι πραγματικός αριθμός.')  
            im = input('Φανταστικό μέρος: ' )
        re, im = str(re), str(im)    
        self.re = str_to_number(re)
        self.im = str_to_number(im)

    def __add__(self,other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        real = self.re * other.re - self.im * other.im
        imaginary = self.im * other.re + self.re * other.im
        return Complex(real, imaginary)

    def len(self):
        length = format(math.sqrt(self.re**2 + self.im**2), '.2f')
        print(float(length))
        return float(length)

    def conjugate(self):
        return Complex(self.re, - self.im)
    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i' 
    

A = Complex('a',2)
# print(A)
# print(is_number('2'))
