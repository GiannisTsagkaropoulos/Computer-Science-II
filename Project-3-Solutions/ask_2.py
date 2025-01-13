def check(type,str):
    while True:
        x = input(str)
        try:
            x = type(x)
        except ValueError as error:
            print(error)
        else: 
            return x
class Polynomial:
    def __init__(self):
        i = 0
        L = []
        flag = 0
        while flag == 0:
            x = check(int,'Give me the coefficient of x^%s: '%(i))
            L.append(x)
            i += 1
            while True:
                try:
                    ans = input('Do you want to continue? ')
                    if ans.lower().strip() in ['y','yes','nai','ναι','ν','yeah']:
                        pass
                    elif ans.lower().strip() in ['n','no','nope','oxi','οχι','ο']:
                        flag = 1
                    else:
                        raise ValueError
                except ValueError:
                    print('Wrong answer. Try again!!!')
                    continue
                else:
                    break
        L.reverse()
        self.__coeff = tuple(L)
    def __add__(self,other):
        n1,n2 = len(self.__coeff),len(other.__coeff)
        M = max(len(self.__coeff),len(other.__coeff))
        self.__coeff = list(self.__coeff)
        other.__coeff = list(other.__coeff)
        for i in range(M-n1):
            self.__coeff.append(0)
        for  j in range(M - n2): 
            other.__coeff.append(0)
        coefficients  = tuple([x + y for (x, y) in zip(self.__coeff,other.__coeff)])
        self.__coeff = coefficients
    def __sub__(self,other):
        n1,n2 = len(self.__coeff),len(other.__coeff)
        M = max(len(self.__coeff),len(other.__coeff))
        self.__coeff = list(self.__coeff)
        other.__coeff = list(other.__coeff)
        for i in range(M-n1):
            self.__coeff.append(0)
        for  j in range(M - n2): 
            other.__coeff.append(0)
        coefficients  = tuple([x - y for (x, y) in zip(self.__coeff,other.__coeff)])
        self.__coeff = coefficients
    def __mul__(self,other):
        self.__coeff = list(self.__coeff) 
        other.__coeff = list(other.__coeff) 
        res = [0]*(len(self.__coeff)+len(other.__coeff)-1)
        for i in range(len(self.__coeff)):
            for j in range(len(other.__coeff)):
                res[i+j] += self.__coeff[i]*other.__coeff[j]
        coefficients = res
        self.__coeff = coefficients
    def __eq__(self,other):
        count = 0
        S = False
        for i in range(len(self.__coeff)):
            if self.__coeff[i] == other.__coeff[i]:
                count += 1 
        if count == len(self.__coeff):
            S = True
        return S
    def evaluate(self):
        ans = check(int,'Give a number so as to evalute the value of the polynomial: ')
        result = 0
        for i in range(len(self.__coeff)):
            result += self.__coeff[i]*(ans**(len(self.__coeff)-1-i))
        return result
    def __str__(self):
        S = ''
        for i in range(len(self.__coeff)):
            if str(self.__coeff[i])[0] != '-':
                S += '+'+str(self.__coeff[i])+'*'+'x^%s'%(len(self.__coeff)-1-i)
            else:
                S += str(self.__coeff[i])+'*'+'x^%s'%(len(self.__coeff)-1-i)
        S = S.lstrip('+')
        return S
