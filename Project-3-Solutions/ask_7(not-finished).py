class Item():

    def __init__(self, title = '' , author = ''):
        while type(title) != str
            print('Ο τίτλος πρέπει να είναι συμβολοσειρά.')
            title = input('Εισαγωγή τίτλου: ')
        while type(author) != str: 
            print('Ο συγγραφέας πρέπει να είναι συμβολοσειρά.')
            author = input('Δώσε ξανά συγγραφέα: ')
        flag = True    
        while flag: #είναι συμβολοσειρά και θα ελέγξω τι σύμβολα περιέχει
            flag = False
            for i in range(len(author)):
                if not( author[i].isalpha() or  author[i] in list(',.-')):
                    print('Η συμβολοσειρά με τον/τους συγγραφέα/συγγραφείς μπορεί μόνο να περιέχει γράμματα ή τα σύμβολα ",", ".", "-".')
                    author = input('Δώσε ξανά συγγραφέα: ')
                    flag = True
                    break                         
        self.title = title
        self.author = author
    
    def __str__(self):
        s1 = 'Τίτλος: ' + str(self.title) + '\n'
        authors = (self.author).split(',')
        if len(authors) == 1:
            s2 = 'Συγγραφεας:' + str(authors[0])
        else:    
            s2 = 'Συγγραφείς: '
            for i in range(len(authors)):
                s2 += str(authors[i])
                if i!=len(authors)-1: #όχι τελευταίο στοιχείο
                    s2 += '\n'
        return s1 + s2

class Book(Item):
    def __init__(self,title = '' , author = '', isbn = '', house = ''):
        Item.__init__(self, title, author)
       #check if isbn is valid 
        while type(isbn) != str:
            print('Το isbn πρέπει να δοθεί σε μορφή συμβολοσειράς.')
            isbn = input('Πληκτρολόγησε ξανά το isbn.')
        isbn_digits = isbn.replace('-','')   
        while isbn.count('-') != 3 or len(isbn_digits) != 13 or not(isbn_digits.isdigit()):
            print('To isbn που έχεις εισάγει δεν είναι έγκυρο.')
            isbn = input('Πληκτρολόγησε ξανά το isbn.')
            isbn_digits = isbn.replace('-','')
        #check if house is valid
        while type(house) != str:
            print('Ο εκδοτικός οίκος bn πρέπει να δοθεί σε μορφή συμβολοσειράς.')
            house = input('Πληκτρολόγησε ξανά τον εκδοτικό οίκο.')
        flag = True    
        while flag: #είναι συμβολοσειρά και θα ελέγξω τι σύμβολα περιέχει. Μπορεί όπως και οι συγγραφείς να περιέχουν ίδια σύμβολα
            flag = False
            for i in range(len(house)):
                if not( house[i].isalpha()  or house[i].isspace() or house[i] in list(',.-')):
                    print('Η συμβολοσειρά με τον/τους συγγραφέα/συγγραφείς μπορεί μόνο να περιέχει γράμματα ή τα σύμβολα ",", ".", "-".')
                    author = input('Δώσε ξανά συγγραφέα: ')
                    flag = True
                    break               
        self.isbn = isbn
        self.house = house

    def __str__(self):    
        title_author = Item.__str__(self)
        s3 = '\nISBN: ' + str(self.isbn)
        s4 = '\nΕκδοτικός Οίκος: ' + str(self.house)
        return title_author + s3 + s4

class Magazine(Item):
    def __init__(self, title = '', author = '', number = ''):
        Item.__init__(self, title, author = 'Συλλογική δουλειά')
        while not(number.isdigit()):
            print('To νούμερο τεύχους δεν είναι έγκυρο.')
            number = input('Παρακαλώ εισάγετε ξανά τον αριθμό του τεύχους: ')
        self.number = number

    def __str__(self):    
        title_author = Item.__str__(self)
        s3 = '\n Νούμερο του τεύχους: ' + str(self.number)
        return title_author + s3

class Thesis(Item): 

    def __init__(self, title, author, epibl, uni):
        Item.__init__(self, title, author)
       #check επιβλέποντα 
        while type(epibl) != str:
            print('Μη έγκυρο όνομα επιβλέποντα.')
            epibl = input('Εισάγετε ξανά το όνομα του επιβλέποντα: ')
        clean_epibl = epibl.replace("'",'')
        clean_epibl = clean_epibl.replace("-",'')
        while not(clean_epibl.isalpha()):
            print('Μη έγκυρο όνομα επιβλέποντα.')
            epibl = input('Εισάγετε ξανά το όνομα του επιβλέποντα: ')
            clean_epibl = epibl.replace("'",'')
            clean_epibl = clean_epibl.replace("-",'')
        #check uni
        while type(uni) != str and not(uni.isalpha()):
            print('Μη έγκυρο όνομα ιδρύματος.')
            uni = input('Εισάγετε ξανά ίδρυμα: ')

        self.epibl = epibl
        self.uni = uni    

    def __str__(self):    
        title_author = Item.__str__(self)
        s3 = '\nΕπιβλέποντας: ' + str(self.epibl)
        s4 = '\nΊδρυμα:  ' + str(self.uni)
        return title_author + s3 + s4    


def menu():
    print('-----------MENU-----------')
    print('1. Βιβλίο')
    print('2. Περιοδικό')
    print('3. Διπλωματική εργασία')

def get_choice():
    choice = input('Επίλεξε αντικείμενο(1,2 ή 3): ')
    while choice not in list('123'):
        print('Μη έγκυρη επιλογή.')    
        choice = input('Επίλεξε ξανά αντικείμενο(1,2 ή 3): ')
    return choice

# def 


leksiko = dict()
acceptable = ['yes','yy','y','ναι','nn','νν','nai','yup','ya','no','nope','όχι','οχι','oxi']
bibliothiki = []
while True:
    answer = input('Θες να εισάγεις κάποιο αντικέιμενο στη βιβλιοθήκη; ')
    while answer.lower() not in acceptable :
        answer = input('Μη έγκυρη απάντηση. Επίλεξε ξανά: ')
    if acceptable.index(answer) >8 : #απάντησε όχι και δεν θέλει να εισάγει άλλο αντικείμενο στη βιβλιοθηκη
        break 
    else: # θέλει να προσθέση κι άλλο
        menu()
        choice = get_choice()
        title = input('Δώσε τίτλο συγγράμματος: ')
        author = input('Δώσε όνομα συγγραφέα (ή συγγραφικής ομάδας, χωρισμένα με κόμμα)')
        if choice == '1':
            item = Book(title, author)
            bibliothiki.append(item)
        elif choice == '2':
            item = Magazine(title, author)
            bibliothiki.append(item)
        elif choice == '3':
            item = Thesis(title, author)
            bibliothiki.append(item)

for i in range(len(bibliothiki)): #δημιουργία λεξικού
    leksiko[i]= bibliothiki[i]

def insert(item):
    global leksiko
    keys_sorted = sorted(list(leksiko.keys())) #με τελευταίο στοιχείο το μεγαλύτερο από όλα
    leksiko[ keys_sorted[len(keys_sorted)-1] + 1 ] = item

# def remov(item)

# choices = {'1': 'Books', '2': 'Magazines', '3': 'Thesis'}
def search():
    while True:
            answer = input('Θες να περιορίσουμε την αναζήτηση σε κάποια συγκεκριμένη  κατηγορία; ')
            while answer.lower() not in acceptable :
                answer = input('Μη έγκυρη απάντηση. Επίλεξε ξανά: ')
            if acceptable.index(answer) >8 : #απάντησε όχι άρα ψάχνω όλο το λεξικό
                
            else: #περιορίζω αναζήτηση σε μία κατηγορία
                print('Σε τι κατηγορία θες να γίνει η αναζήτηση;')
                menu()
                choice = input('Η επιλογή μου είναι: ')
                while not (choice.isdigit() ):
                    print('Μη έγκυρη επιλογή.')
                    choice = input('Η επιλογή μου είναι: ')
                if choice == '1':
                    for key in leksiko:
                        if type(leksiko[key]) == Book and leksiko[key].title == title:
    FOUND = False
    print('Αναζήτηση ως προς: \n 1. Τίτλο \n 2. Συγγραφέα')
    epilogi = input('Η επιλογή μου είναι(1 ή 2): ')
    while not (epilogi.isdigit() ):
                    print('Μη έγκυρη επιλογή.')
                    epilogi = input('Η επιλογή μου είναι(1 ή 2): ')
    if epilogi == '1': #Αναζήτηση ως προς τίτλο
        title = input('Τίτλος σύμφωνα με τον οποίο θα γίνει η αναζήτηση: ')
        for key in leksiko:
            if leksikop[key].title == title:
                FOUND = True
                break                
    else: #Αναζήτηση ως προς συγγραφέα
        author = input('Δώσε συγγραφέα σύμφωνα με τον οποίο θα γίνει η αναζήτηση: ')
        #έλεγχος για άκυρα σύμβολα
        flag = True    
        while flag: #είναι συμβολοσειρά και θα ελέγξω τι σύμβολα περιέχει
            flag = False
            for i in range(len(author)):
                if not( author[i].isalpha() or  author[i] in list(',.-')):
                    print('Η συμβολοσειρά με τον/τους συγγραφέα/συγγραφείς μπορεί μόνο να περιέχει γράμματα ή τα σύμβολα ",", ".", "-".')
                    author = input('Δώσε ξανά συγγραφέα: ')
                    flag = True
                    break
        ###
        for key in leksiko:
            if leksiko[key].author == author:
                FOUND = True 
                    



        # acceptable = ['yes','yy','y','ναι','nn','νν','nai','yup','ya','no','nope','όχι','οχι','oxi']
        
        while True:
            answer = input('Θες να περιορίσουμε την αναζήτηση σε κάποια συγκρικριμένη  κατηγορία; ')
            while answer.lower() not in acceptable :
                answer = input('Μη έγκυρη απάντηση. Επίλεξε ξανά: ')
            if acceptable.index(answer) >8 : #απάντησε όχι άρα ψάχνω όλο το λεξικό
                
            else: #περιορίζω αναζήτηση σε μία κατηγορία
                print('Σε τι κατηγορία θες να γίνει η αναζήτηση;')
                menu()
                choice = input('Η επιλογή μου είναι: ')
                while not (choice.isdigit() ):
                    print('Μη έγκυρη επιλογή.')
                    choice = input('Η επιλογή μου είναι: ')
                if choice == '1':
                    for key in leksiko:
                        if type(leksiko[key]) == Book and leksiko[key].title == title:
                            


