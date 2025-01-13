import pickle
import datetime 
monthdays = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8: 31, 9:30, 10:31, 11:30, 12:31}

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
class Artist:
    def __init__(self, name = '', country = '', dob = ''):
        while type(name) != str:
            print('Μη έγκυρο όνομα.')
            name = input('Δώσε ξανά το όνομα του καλλιτέχνη: ')
        while type(country) != str and not(country.isalpha()): 
            print('Μη έγκυρο όνομα.')
            country = input('Δώσε ξανά τη χώρα καταγωγής του καλλιτέχνη: ')      
        if type(dob) != str :
            print('Μη αποδεκτός τύπος δεδομένου για την ημερομηνία γέννησης.')
            dob = input('Δώσε ξανά την ημερομηνία γέννησης του καλλιτέχνη (day/month/year):  ').split('/')
        else: 
            dob = dob.split('/')   
        while True:   
            flag = True        
            if len(dob) == 3 :
                try:
                    for i in range(len(dob)):
                        dob[i] = int(dob[i])
                    if dob[1]<0 or dob[1]>13:
                        print(f'Δεν υπάρχει {dob[1]}ος μήνας') 
                        flag = False
                    elif dob[0]<0 or dob[0] > monthdays[ dob[1] ]: #ημέρες μήνα αρνητικές ή περισσότερες από όσες μέρες έχει ο μήνας
                        print(f'Δεν γίνεται ο {dob[1]}ος μήνας να έχει {dob[0]} μέρες.')
                        flag = False    
                    elif  dob[2]> datetime.date.today().year or dob[2]<datetime.date.today().year - 118: #γεννημένος μετά το έτος μας ή έχει ηλικία μεγαλύτερη των 118 χρονών   
                        print('Δε δεχόμαστε φαντάσματα καλλιτέχνες.')
                        flag = False
                    if flag == True:
                        break
                    else: 
                        dob = input('Δώσε ξανά την ημερομηνία γέννησης του καλλιτέχνη (day/month/year):  ').split('/')
                except ValueError:
                    print('Οι ημερομηνία γέννησης του καλλιτέχνη πρέπει είναι της μορφής (day/month/year).') 
                    dob = input('Δώσε ξανά την ημερομηνία γέννησης του καλλιτέχνη (day/month/year):  ').split('/')      
            else:
                dob = input('Δώσε ξανά την ημερομηνία γέννησης του καλλιτέχνη (day/month/year):  ').split('/')
        dob = [str(i) for i in dob]  
        dob = '/'.join(dob)   
        self.name = name
        self.country = country
        self.dob = dob

    def __str__(self):
        s1 = 'Name: ' + self.name + '\n'
        s2 = 'Country: ' + self.country + '\n'
        s3 = 'Birthday: ' + self.birthday
        return s1 + s2 + s3
class item:
    def __init__(self,discname,artist,label,gerne,type):
        self.discname = discname
        if isinstance(artist,Artist):
            self.artist = artist
        else:
            raise AttributeError('artist must be an object from the class Artist')
        self.label = label
        self.gerne = gerne
        self.type = type
    def __str__(self):
        s1 = 'Disc Name: ' + self.discname +'\n'
        s2 = 'Artist: ' +'Name: ' + self.artist.name + '\n' +'        Country: ' + self.artist.country + '\n' + '        Birthday: ' + self.artist.birthday +'\n'
        s3 = 'Label: ' + self.label + '\n'
        s4 = 'Gerne: ' + self.gerne + '\n'
        s5 = 'Type: ' + self.type
        return s1+ s2+ s3 + s4 + s5
try:
    f = open('ask_8.bin','rb')
    art,it = pickle.load(f)
except FileNotFoundError:
    f = open('ask_8.bin','wb')
    art = []
    it = []
    L = [art,it]
flag = 0
while flag == 0:
    print('-'*10 + 'Menu' + '-'*10)
    print('1) Εισαγωγή αντικειμένου')
    print('2) Διαγραφή αντικειμένου')
    print('3) Αναζήτηση ως προς τίτλο και προβολή των στοιχείων του δίσκου.')
    print('4) Προβολή δισκογραφίας: αναζήτηση ως προς όνομα καλλιτέχνη και προβολή όλων των δίσκων του καλλιτέχνη')
    ans = MenuCheck('Pick an action from the Menu by typing the number: ',1,4)
    if ans == 1:
        name = input('Name: ').strip()
        for i in it:
            if i.discname == name:
                print('There is already a disc by the name:',name)
                break
        else:
            artname = input('Artist Name: ').strip()
            for i in art:
                if artname == i.name:
                    print('There is already an artist by the name:',artname,'so you dont need to fill up the rest of the information of the artist')
                    print('Just fill up the rest information for the disc!')
                    label = input('Label: ')
                    gerne = input('Gerne: ')
                    type = input('Type: ')
                    it.append(item(name,Artist(i.name,i.country,i.birthday),label,gerne,type))
                    break
            else:
                artcountry = input('Artist Country: ')
                artbirthday = input('Artist birthday: ')
                label = input('Label: ')
                gerne = input('Gerne: ')
                type = input('Type: ')
                it.append(item(name,Artist(artname,artcountry,artbirthday),label,gerne,type))
                for j in art:
                    if j.name == artname:
                        break
                else:
                    art.append(Artist(artname,artcountry,artbirthday))
    elif ans == 2:
        name = input('Name: ')
        for i in range(len(it)):
            if it[i].discname == name:
                del it[i]
                break
    elif ans == 3:
        name = input('Name: ')
        for i in it:
            if i.discname == name:
                print(i)
                break
        else:
            print('There isnt a disc by the name:',name)
    elif ans == 4:
        name = input('Artist Name: ')
        S = []
        flag1 = 0
        for j in art:
            S.append(j.name)
        if  name in S:
            for i in it:
                if i.artist.name == name:
                    print('Disc: ',i.discname)
                    flag1 = 1
            if flag1 == 0:
                print('No Discs from the artist:',name)
        else:
            print('There isn\'t an artist called:',name)
    while True:
        end = input('Do you want to do another action?')
        try:    
            if end.lower().strip() in ['y','yes','nai','ναι','ν','yeah']:
                pass
            elif end.lower().strip() in ['n','no','oxi','οχι','ο','nope']:
                f = open('ask_8','wb')
                L = [art,it]
                pickle.dump(L,f)
                flag = 1
            else:
                raise ValueError
        except ValueError:
            print('I cant understand what are you saying. Try again!!!')
            continue
        else:
            break



 