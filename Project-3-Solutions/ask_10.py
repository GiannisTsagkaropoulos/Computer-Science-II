import pickle
def check(type,str):
    while True:
        x = input(str)
        try:
            x = type(x)
        except ValueError as error:
            print(error)
        else: 
            return x
def MenuCheck(str,x,y):
    while True:
        ans = input(str)
        try:
            ans = int(ans)
            if ans > y or ans < x:
                raise AttributeError
        except ValueError as error:
            print(error)
        except AttributeError: 
            print('The number should be between %s and %s'%(x,y))
        else:
            return ans
class Person:
    def __init__(self,name,email,subscribed):
        self.__name = name
        self.__email = email
        self.__subscribed = subscribed
    def get_name(self):
        return self.__name
    def get_Sub(self):
        return self.__subscribed
    def get_Em(self):
        return self.__email
    def __str__(self):
        s1 = 'Name: '+self.__name+'\n'
        s2 = 'Email: '+self.__email + '\n'
        s3 = 'Subscribed: ' + str(self.__subscribed)
        return s1 + s2 + s3
class CLient(Person):
    def __init__(self,name,email,subscribed,AFM):
        Person.__init__(self,name,email,subscribed)
        self.__AFM = AFM
    def changeS(self,subscribed):
        self._Person__subscribed = subscribed
    def changeEmail(self,email):
        self._Person__email = email
    def __str__(self):
        s4 = '\n' + 'AFM: '+self.__AFM
        return Person.__str__(self) + s4
class Personel(Person):
    def __init__(self,name,email,role,subscribed = True):
        Person.__init__(self,name,email,subscribed)
        self.__role = role
    def  changeRole(self,role):
        self.__role = role
    def __str__(self):
        s4 = '\n' + 'Role: '+self.__role
        return Person.__str__(self) + s4
try:
    f = open('ask_10.bin','rb')
    Cl,Pers = pickle.load(f)
except FileNotFoundError:
    f = open('ask_10.bin','wb')
    Cl = []
    Pers = []
    L = [Cl,Pers]
flag = 0
while flag == 0:
    print('-'*10+'Menu'+'-'*10)
    print('1) Εισαγωγή πελάτη/μέλος του προσωπικού')
    print('2) Αλλαγή email πελάτη')
    print('3) Αλλαγή τιμή στο πεδίο subscribed του πελάτη')
    print('4) Διαγραφή πελάτη/μέλος του προσωπικού')
    print('5) Επιστροφή συμβολοσειράς με τα email όσον έχουν subscribed == True.')
    ans = MenuCheck('Pick an action from the Menu by typing the number: ',1,5)
    if ans == 1:
        print('1) Client')
        print('2) Personel')
        ans1 = MenuCheck('Pick the type of the entry: ',1,2)
        if ans1 == 1: 
            name = input('Name: ').strip()
            email = input('Email: ')
            subscribed = MenuCheck('''Subscribed 1) True 
           2) False: ''',1,2)
            AFM = check(int,'AFM: ')
            Cl.append(CLient(name,email,subscribed,AFM))
        elif ans1 == 2:
            name = input('Name: ').strip()
            email = input('Email: ')
            role = input('Role: ')
            Pers.append(Personel(name,email,role))
    elif ans == 2:
        name = input('Name: ').strip()
        for i in Cl:
            if i.get_name() == name:
                email = input('New Email: ')
                i.changeEmail(email)
                break
        else:
            print('there isn\'t a Client named: ',name)
    elif ans == 3:
        name = input('Name: ').strip()
        for i in Cl:
            if i.get_name() == name:
                subscribed = MenuCheck('''Subscribed 1) True 
           2) False: ''',1,2)
                i.changeS(subscribed)
                break
        else:
            print('there isn\'t a Client named: ',name)
    elif ans == 4:
        print('1) Client')
        print('2) Personel')
        ans2 = MenuCheck('Pick the type of the entry: ',1,2)
        if ans2 == 1: 
            name = input('Name: ').strip()
            for i in range(len(Cl)):
                if Cl[i].get_name() == name:
                    del Cl[i]
                    break
            else:
                print('there isn\'t a Client named: ',name)
        elif ans2 == 2:
            name = input('Name: ').strip()
            for i in range(len(Pers)):
                if Pers[i].get_name() == name:
                    del Pers[i]
                    break
            else:
                print('there isn\'t a Personel named: ',name)
    elif ans == 5:
        S = ''
        for i in Cl:
            if i.get_Sub() == 1:
                S += str(i.get_Em()) + ','
        print(S)
    while True:
        end = input('Do you want to do another action?')
        try:    
            if end.lower().strip() in ['y','yes','nai','ναι','ν','yeah']:
                pass
            elif end.lower().strip() in ['n','no','oxi','οχι','ο','nope']:
                f = open('ask_10','wb')
                L = [Cl,Pers]
                pickle.dump(L,f)
                flag = 1
            else:
                raise ValueError
        except ValueError:
            print('I cant understand what are you saying. Try again!!!')
            continue
        else:
            break
