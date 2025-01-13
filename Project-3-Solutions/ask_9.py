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
class Books: 
    def __init__(self,title,price,quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
    def __str__(self):
        s1 = 'Title: ' + str(self.title) + '\n'
        s2 = ' '*11 +'Price: ' + str(self.price) + '\n'
        s3 = ' '*11 +'Quantity: ' + str(self.quantity)
        return s1+s2+s3
class Stationery:
    def __init__(self,model,price,quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
    def __str__(self):
        s1 = 'Model: ' + str(self.model) + '\n'
        s2 = ' '*11 +'Price: ' + str(self.price) + '\n'
        s3 = ' '*11 +'Quantity: ' + str(self.quantity)
        return s1+s2+s3
class Stationery1:
    def __init__(self,model,price,quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
    def __str__(self):
        s1 = 'Model: ' + str(self.model) + '\n'
        s2 = ' '*11 +'Price: ' + str(self.price) + '\n'
        s3 = ' '*11 +'Quantity: ' + str(self.quantity)
        return s1+s2+s3
class LitBooks(Books):
    def __init__(self,title,price,quantity,minquan):
        Books.__init__(self,title,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+ ' '*11 +'Minimum Quantity: ' + str(self.minquan)
        return Books.__str__(self) + s4
class SchBooks(Books):
    def __init__(self,title,price,quantity,minquan):
        Books.__init__(self,title,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+ ' '*11 +'Minimum Quantity: ' + str(self.minquan)
        return Books.__str__(self) + s4
class Pens(Stationery):
    def __init__(self,model,price,quantity,minquan):
        Stationery.__init__(self,model,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+' '*11+ 'Minimum Quantity: ' + str(self.minquan)
        return Stationery.__str__(self) + s4
class Pencil(Stationery):
    def __init__(self,model,price,quantity,minquan):
        Stationery.__init__(self,model,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+' '*11 + 'Minimum Quantity: ' + str(self.minquan)
        return Stationery.__str__(self) + s4
class SketchBlock(Stationery1):
    def __init__(self,model,price,quantity,minquan):
        Stationery1.__init__(self,model,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+ ' '*11 +'Minimum Quantity: ' + str(self.minquan)
        return Stationery1.__str__(self) + s4
class A4(Stationery1):
    def __init__(self,model,price,quantity,minquan):
        Stationery1.__init__(self,model,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+ ' '*11 +'Minimum Quantity: ' + str(self.minquan)
        return Stationery1.__str__(self) + s4
class NoteBook(Stationery1):
    def __init__(self,model,price,quantity,minquan):
        Stationery1.__init__(self,model,price,quantity)
        self.minquan = minquan
    def __str__(self):
        s4 = '\n'+' '*11 + 'Minimum Quantity: ' + str(self.minquan)
        return Stationery1.__str__(self) + s4
try:
    f = open('ask_9.bin','rb')
    L = pickle.load(f)
except FileNotFoundError:
    f = open('ask_9.bin','wb')
    L = [[[],[],[]],[[],[],[]],[[],[],[],[]]]
flag = 0
while flag == 0:
    print('-'*10+'Menu'+'-'*10)
    print('1) Εισαγωγή αντικειμένου')
    print('2) Αλλαγή ποσότητας αντικειμένου')
    print('3) Αλλαγή τιμής αντικειμένου')
    print('4) Διαγραφή αντικειμένου')
    print('''5) Αναζήτηση και εμφάνιση των 
    αντικειμένων που η ποσότητά 
    τους είναι μικρότερη από την 
    ελάχιστη ποσότητα.''')
    print('6) Προβολή λίστας προϊόντων ανά κατηγορία.')
    ans = MenuCheck('Pick an action from the Menu by typing the number: ',1,6)
    if ans == 1:
        print('-'*10+'Menu'+'-'*10)
        print('1) Book')
        print('2) Stationary(Writing Type)')
        print('3) Stationary(Paper Type)')
        ans1 = MenuCheck('Pick the type of the product from the Menu by typing the number: ',1,3)
        if ans1 == 1:
            print('-'*10+'Menu Books'+'-'*10)
            print('1) Literature Book')
            print('2) School Book')
            print('3) Other type of Book')
            ans2 = MenuCheck('Pick type of the book from the Menu Books by typing the number: ',1,3)
            if ans2 == 1:
                title = input('Give the title of the book: ').strip()
                for i in L[0][0]:
                    if i.title == title:
                        print('There is already a book by the name of: ',title)
                        break
                else:
                    price = check(float,'Give the price of the book: ')
                    quantity = check(int,'Give the quantity of the book: ')
                    minquan = check(int,'Give the minimum quantity of the book: ')
                    L[0][0].append(LitBooks(title,price,quantity,minquan))
            elif ans2 == 2:
                title = input('Give the title of the book: ').strip()
                for i in L[0][1]:
                    if i.title == title:
                        print('There is already a book by the name of: ',title)
                        break
                else:
                    price = check(float,'Give the price of the book: ')
                    quantity = check(int,'Give the quantity of the book: ')
                    minquan = check(int,'Give the minimum quantity of the book: ')
                    L[0][1].append(SchBooks(title,price,quantity,minquan))
            elif ans2 == 3:
                title = input('Give the title of the book: ').strip()
                for i in L[0][2]:
                    if i.title == title:
                        print('There is already a book by the name of: ',title)
                        break
                else:
                    price = check(float,'Give the price of the book: ')
                    quantity = check(int,'Give the quantity of the book: ')
                    L[0][2].append(Books(title,price,quantity))
        elif ans1 == 2:
            print('-'*10+'Menu Stationary(Writing Type)'+'-'*10)
            print('1) Pen')
            print('2) Pencil')
            print('3) Other type of Stationary(Writing Type)')
            ans3 = MenuCheck('Pick the type of the Stationary(Writing Type) from the Menu Stationary(Writing Type) by typing the number: ',1,3)
            if ans3 == 1:
                model = input('Give the model of the Pen: ').strip()
                for i in L[1][0]:
                    if i.model == model:
                        print('There is already a Pen by the name of: ',model)
                        break
                else:        
                    price = check(float,'Give the price of the Pen: ')
                    quantity = check(int,'Give the quantity of the Pen: ')
                    minquan = check(int,'Give the minimum quantity of the Pen: ')
                    L[1][0].append(Pens(model,price,quantity,minquan))
            elif ans3 == 2:
                model = input('Give the model of the Pencil: ').strip()
                for i in L[1][1]:
                    if i.model == model:
                        print('There is already a Pencil by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the Pencil: ')
                    quantity = check(int,'Give the quantity of the Pencil: ')
                    minquan = check(int,'Give the minimum quantity of the Pencil: ')
                    L[1][1].append(Pencil(model,price,quantity,minquan))
            elif ans3 == 3:
                model = input('Give the model of the Stationary(Writing Type): ').strip()
                for i in L[1][2]:
                    if i.model == model:
                        print('There is already a Stationary(Writing Type) product by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the Stationary(Writing Type): ')
                    quantity = check(int,'Give the quantity of the Stationary(Writing Type): ')
                    L[1][2].append(Stationery(model,price,quantity))
        elif ans1 == 3:
            print('-'*10+'Menu Stationary(Paper Type)'+'-'*10)
            print('1) Sketch Block')
            print('2) Note Book')
            print('3) A4')
            print('4) Other type of Stationary(Paper Type)')
            ans4 = MenuCheck('Pick a type of the Stationary(Paper Type) from the Menu Stationary(Paper Type) by typing the number: ',1,4)
            if ans4 == 1:
                model = input('Give the model of the Sketch Block: ').strip()
                for i in L[2][0]:
                    if i.model == model:
                        print('There is already a Stationary(Paper Type) product by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the Sketch Block: ')
                    quantity = check(int,'Give the quantity of the Sketch Block: ')
                    minquan = check(int,'Give the minimum quantity of the Sketch Block: ')
                    L[2][0].append(SketchBlock(model,price,quantity,minquan))
            elif ans4 == 2:
                model = input('Give the model of the Note Book: ').strip()
                for i in L[2][0]:
                    if i.model == model:
                        print('There is already a Stationary(Paper Type) product by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the Note Book: ')
                    quantity = check(int,'Give the quantity of the Note Book: ')
                    minquan = check(int,'Give the minimum quantity of the Note Book: ')
                    L[2][1].append(NoteBook(model,price,quantity,minquan))
            elif ans4 == 3:
                model = input('Give the model of the A4: ').strip()
                for i in L[2][0]:
                    if i.model == model:
                        print('There is already a Stationary(Paper Type) product by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the A4: ')
                    quantity = check(int,'Give the quantity of the A4: ')
                    minquan = check(int,'Give the minimum quantity of the A4: ')
                    L[2][2].append(A4(model,price,quantity,minquan))
            elif ans4 == 4:
                model = input('Give the model of the Stationary(Paper Type): ').strip()
                for i in L[2][0]:
                    if i.model == model:
                        print('There is already a Stationary(Paper Type) product by the name of: ',model)
                        break
                else:
                    price = check(float,'Give the price of the Stationary(Paper Type): ')
                    quantity = check(int,'Give the quantity of the Stationary(Paper Type): ')
                    L[2][3].append(Stationery1(model,price,quantity))
    elif ans == 2:
        print('Of what thing do you want to change the quantity?')
        print('-'*10+'Menu'+'-'*10)
        print('1) Book')
        print('2) Stationary(Writing Type)')
        print('3) Stationary(Paper Type)')
        ans5 = MenuCheck('Pick an action from the Menu by typing the number: ',1,3)
        if ans5 == 1:
            print('-'*10+'Menu Books'+'-'*10)
            print('1) Literature Book')
            print('2) School Book')
            print('3) Other type of Book')
            ans6 = MenuCheck('Pick a type from the Menu Books by typing the number: ',1,3)
            tit = input('Give the title of the book ').strip()
            for i in L[0][ans6-1]:
                if i.title == tit:
                    newquan = check(int,'What is the new quantity? ')
                    i.quantity = newquan
                    break
            else:
                print('The title of the book you gave doesnt exist!!!')
        elif ans5 == 2:
            print('-'*10+'Menu Stationary(Writing Type)'+'-'*10)
            print('1) Pen')
            print('2) Pencil')
            print('3) Other type of Stationary(Writing Type)')
            ans7 = MenuCheck('Pick the type of the Stationary(Writing Type) from the Menu Stationary(Writing Type) by typing the number: ',1,3)
            nam = input('Give the model of the Stationary(Writing Type)').strip()
            for i in L[1][ans7-1]:
                if i.model == nam:
                    newquan = check(int,'What is the new quantity? ')
                    i.quantity = newquan
                    break
            else:
                print('The model of the Stationary(Writing Type) you gave doesnt exist!!!')
        elif ans5 == 3:
            print('-'*10+'Menu Stationary(Paper Type)'+'-'*10)
            print('1) Sketch Block')
            print('2) Note Book')
            print('3) A4')
            print('4) Other type of Stationary(Paper Type)')
            ans8 = MenuCheck('Pick the type of the Stationary(Writing Type) from the Menu Stationary(Paper type) by typing the number: ',1,4)
            nam = input('Give the model of the Stationary(Paper Type)').strip()
            for i in L[2][ans8-1]:
                if i.model == nam:
                    newquan = check(int,'What is the new quantity? ')
                    i.quantity = newquan
                    break
            else:
                print('The model of the Stationary(Paper Type) you gave doesnt exist!!!')
    elif ans == 3:
        print('Of what thing doyou want to change the price?')
        print('-'*10+'Menu'+'-'*10)
        print('1) Book')
        print('2) Stationary(Writing Type)')
        print('3) Stationary(Paper Type)')
        ans9 = MenuCheck('Pick the type of the product from the Menu by typing the number: ',1,3)
        if ans9 == 1:
            print('-'*10+'Menu Books'+'-'*10)
            print('1) Literature Book')
            print('2) School Book')
            print('3) Other type of Book')
            ans10 = MenuCheck('Pick a type from the Menu Books by typing the number: ',1,3)
            tit = input('Give the title of the book').strip()
            for i in L[0][ans10-1]:
                if i.title == tit:
                    newprice = check(int,'What is the new price? ')
                    i.price = newprice
                    break
            else:
                print('The title of the book you gave doesnt exist!!!')
        elif ans9 == 2:
            print('-'*10+'Menu Stationary(Writing Type)'+'-'*10)
            print('1) Pen')
            print('2) Pencil')
            print('3) Other type of Stationary(Writing Type)')
            ans11 = MenuCheck('Pick an action from the Menu Stationary(Writing Type) by typing the number: ',1,3)
            nam = input('Give the model of the Stationary(Writing Type)').strip()
            for i in L[1][ans11-1]:
                if i.model == nam:
                    newprice = check(int,'What is the new price? ')
                    i.price = newprice
                    break
            else:
                print('The model of the Stationary(Writing Type) you gave doesnt exist!!!')
        elif ans9 == 3:
            print('-'*10+'Menu Stationary(Paper Type)'+'-'*10)
            print('1) Sketch Block')
            print('2) Note Book')
            print('3) A4')
            print('4) Other type of Stationary(Paper Type)')
            ans12 = MenuCheck('Pick an action from the Menu Stationary(Paper Type) by typing the number: ',1,4)
            nam = input('Give the model of the Stationary(Paper Type)').strip()
            for i in L[2][ans12-1]:
                if i.model == nam:
                    newprice = check(int,'What is the new price? ')
                    i.price = newprice
                    break
            else:
                print('The model of the Stationary(Paper Type) you gave doesnt exist!!!')
    elif ans == 4:
        print('what type of thing do you want to delete?')
        print('-'*10+'Menu'+'-'*10)
        print('1) Book')
        print('2) Stationary(Writing Type)')
        print('3) Stationary(Paper Type)')
        ans9 = MenuCheck('Pick the type of the product from the Menu by typing the number: ',1,3)
        if ans9 == 1:
            print('-'*10+'Menu Books'+'-'*10)
            print('1) Literature Book')
            print('2) School Book')
            print('3) Other type of Book')
            ans10 = MenuCheck('Pick a type from the Menu Books by typing the number: ',1,3)
            tit = input('Give the title of the book').strip()
            for i in range(len(L[0][ans10-1])):
                if L[0][ans10-1][i].title == tit:
                    del L[0][ans10-1][i]
                    break
            else:
                print('The title of the book you gave doesnt exist!!!')
        elif ans9 == 2:
            print('-'*10+'Menu Stationary(Writing Type)'+'-'*10)
            print('1) Pen')
            print('2) Pencil')
            print('3) Other type of Stationary(Writing Type)')
            ans11 = MenuCheck('Pick an action from the Menu Stationary(Writing Type) by typing the number: ',1,3)
            nam = input('Give the model of the Stationary(Writing Type)').strip()
            for i in range(len(L[1][ans11-1])):
                if L[1][ans11-1][i].model == nam:
                    del L[1][ans11-1][i]
                    break
            else:
                print('The model of the Stationary(Writing Type) you gave doesnt exist!!!')
        elif ans9 == 3:
            print('-'*10+'Menu Stationary(Paper Type)'+'-'*10)
            print('1) Sketch Block')
            print('2) Note Book')
            print('3) A4')
            print('4) Other type of Stationary(Paper Type)')
            ans12 = MenuCheck('Pick an action from the Menu Stationary(Paper Type) by typing the number: ',1,4)
            nam = input('Give the model of the Stationary(Paper Type)').strip()
            for i in range(len(L[2][ans12-1])):
                if L[2][ans12-1][i].model == nam:
                    del L[2][ans12-1][i]
                    break
            else:
                print('The model of the Stationary(Paper Type) you gave doesnt exist!!!')
    elif ans == 5:
        for i in L:
            for j in i:
                for k in j:
                    if k.quantity < k.minquan:
                        print(k)
    elif ans == 6:
        D = {'Books':['Literature Books','School Books','Other Books'],'Stationary(Writing Type)':['Pen','Pencil','Other Stationary(Writing Type)'],'Stationary(Paper Type)':['Sketch Block','Note Book','A4','Other Stationary(Paper Type)']}
        for i,l in enumerate(list(D.keys())):
            print(l)
            for j,k in enumerate(D[l]):
                print(' '*5+k)
                count = 1
                for n in L[i][j]:
                    print(' '*8 + str(count) + ') ', end = '')
                    print(n)
                    count += 1
    while True:
        end = input('Do you want to do another action?')
        try:    
            if end.lower().strip() in ['y','yes','nai','ναι','ν','yeah']:
                pass
            elif end.lower().strip() in ['n','no','oxi','οχι','ο','nope']:
                f = open('ask_9','wb')
                pickle.dump(L,f)
                flag = 1
            else:
                raise ValueError
        except ValueError:
            print('I cant understand what are you saying. Try again!!!')
            continue
        else:
            break

