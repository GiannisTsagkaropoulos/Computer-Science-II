import datetime
import os 
from readline import set_completion_display_matches_hook
from typing import Counter

months = {1:'Ιανουάριο', 2:'Φεβρουάριο', 3:'Μάρτιο',4:'Απρίλιο',5:'Μάιο',6:'Ιούνιο'\
    ,7:'Ιούλιο',8:'Αύγουστο',9:'Σεπτέμρβιο',10:'Οκτώμβριο',11:'Νοέμβριο',12:'Δεκέμβριο'}    

# Το μενού
def menu():
    print('\n-----------------ΜΕΝΟΥ-----------------\n')
    print('1) Αρχική καταγραφή εξόδων')
    print('2) Προσθήκη εξόδου για τρέχoν μήνα')
    print('3) Αλλαγή εξόδων για παλαιότερο μήνα')
    print('4) Συνολικά έξοδα για περίοδο προηγούμενου έτους')
    print('5) Τρέχον μέσος όρος εξόδων')
    print('6) Τερματισμός\n')

# Η επιλογή του χρήστη
def get_choice():
    return input('Δώσε την επιλογή σου: ')
    
def give_expenses(index,akoma):
    if akoma: #akoma = True or False, 
        print('Πόσα έξοδα είχες ακόμα τον ',months[index], '(Εισαγωγή θετικού αριθμού): ', end = '')
    else:
        print('Πόσα έξοδα είχες τον ',months[index], '(Εισαγωγή θετικού αριθμού): ', end = '')
    expenses = input()  
    while True:
        try:
            expenses = float(expenses)
            break            
        except ValueError as error:
            print(error)  
            if akoma:
                print('Μη έγκυρη επιλογή. Πόσα έξοδα είχες ακόμα τον ',months[index], '(Εισαγωγή θετικού αριθμού): ', end = '') #input 1 arg',months[index], '(Εισαγωγή θετικού αριθμού): ')
            else:
               print('Μη έγκυρη επιλογή. Πόσα έξοδα είχες τον ',months[index], '(Εισαγωγή θετικού αριθμού): ', end = '') 
            expenses = input()
    return abs(expenses)

def give_file_name():
    name = input('Δώσε το όνομα που επιθυμείς να έχει το αρχείο (χωρίς κατάληξη): ')
    while len(name.split()) != 1 or len(name.split('.')) !=1 :#more than 2 words, or has κατάληξη
         name = input('Μη έγκυρη επιλογή ονόματος. Δώσε ξανά όνομα για το αρχείο: ')  
    return name   

def give_directory_name():
    while True:
        dir_name = input('Δώσε το directory στο οποίο επιθυμείς να δημιουργηθεί το αρχείο: ') #το δίνει μαζί με το όνομα του αρχείο 
        if os.path.isdir(dir_name) : #είναι directory
            the_path = dir_name
            break
        else:     
                print('Αυτό που έδωσες δεν αποτελεί path κάποιου directory!')   
    return the_path 

def give_pathname():
    while True:
        path_name = input('Δώσε το pathname που επιθυμείς να έχει το αρχείο: ') #το δίνει μαζί με το όνομα του αρχείο 
        if os.path.isfile(path_name) : #είναι αρχείο
            the_path = path_name
            break
        else:     
                print('Αυτό που έδωσες δεν αποτελεί path κάποιου αρχείου!')   
    return the_path 

# Επιλογή 1: Αρχική καταγραφή εξόδων
def write_expenses_from_scratch(my_path):
    name = give_file_name() #όνομα χωρίς κατάληξη
    full_path =  my_path + '/' + name + '.csv' 
    f = open(full_path,'w')
    f.write('Μήνες, Έξοδα \n')
    for i in range(1,13):
        if i <= datetime.date.today().month:
            expenses = give_expenses(i,False) #θα εκτυπώσει μήνυμα χωρίς το "ακόμα"
            f.write(months[i] + ',' + str(expenses)+'\n')
        else:
            f.write(months[i]+','+'0\n')

# Επιλογή 2: Προσθήκη εξόδου για τρέχoν μήνα
def add_this_month(filename):
    f = open(filename, 'r')
    month = datetime.date.today().month
    expense = give_expenses(month,True) #θα εκτυπώσει μήνυμα με "ακόμα"
    counter = -1 #θα μετράει πόσες γραμμές έχουν διαβαστεί. Θέλω counter να είναι 1 για Ιανουάριο, 2 για Φεβρ. ... Και έχω και heading.
    text, changed = '', ''
    for line in f:
        counter += 1
        if counter != month:
            text += line
        else:    
            words = line.split(',') #['month', '123\n']
            changed += words[0] + ',' + str(float(words[1])+expense)+'\n'  
            text += changed
    f.close()
    f = open(filename, 'w')
    f.write(text)
    f.close()
    #/Users/giannistsagaropoulos/Desktop/pi.

# Επιλογή 3: Αλλαγή εξόδων για παλαιότερο μήνα
def change_exp(filename):
    while True:
        print('Σε ποιον μήνα, πριν τον', months[datetime.date.today().month], 'θες να πραγματοποιήσεις αλλαγή εξόδων(π.χ. Ιανουάριο). Στον :  ', end = '')
        month = input()
        while month not in list(months.values()):
            print('Μη έγκυρη επιλογή. Σε ποιον μήνα, πριν τον', months[datetime.date.today().month], 'θες να πραγματοποιήσεις αλλαγή εξόδων; Στον: ', end = '')
            month = input()
        for i in range(1,13):
            if months[i] == month:
                month = i #if month = june, θα γίνει month = 6
                break
        if  month < datetime.date.today().month: #είναι παλαιότερος
            break
        else:
            print('Πρέπει να εισάγεις παλαιότερο μήνα από τον ',months[datetime.date.today().month] )
    expenses = give_expenses(month, False)  #positive number, θα εμφανίσει μήνυμα χωρίς το "ακόμα"
    f= open(filename, 'r') 
    lines = f.readlines() #list with text lines.
    f.close()
    f= open(filename, 'w')
    for i in range(13): 
        if i!=month:
            f.write(lines[i])
        else:
            f.write(months[i] + ',' + str(expenses) + '\n')     

# Επιλογή 4: Συνολικά έξοδα για περίοδο του έτους:
def sum_of_expenses_for_year(filename):
    while True:
        starting_month = input('Με ποιον μήνα θες να ξεκινάει η καταμέτρηση των εξόδων; Με τον: ')
        while starting_month not in list(months.values()):
            starting_month = input('Μη έγκυρη επιλογή. Με ποιον μήνα θες να ξεκινάει η καταμέτρηση των εξόδων; Με τον: ')
        ending_month = input('Με ποιον μήνα θες να τελειώνει η καταμέτρηση των εξόδων; Με τον: ')
        while ending_month not in list(months.values()):
            ending_month = input('Μη έγκυρη επιλογή. Με ποιον μήνα θες να τελειώνει η καταμέτρηση των εξόδων; Με τον: ')    
        #πρέπει να ελέγξω αν ο starting προηγείται
        for i in range(1,13):
            if starting_month == months[i]:
                starting_month = i #if starting_month = june, θα γίνει starting_month = 6
            elif ending_month == months[i]:
                ending_month = i
        if ending_month < starting_month:
            print('Δε γίνεται ο μήνας στον οποίο θα τελειώσει η καταμέτρηση των εξόδων να προηγείται του μήνα στον οποίο ξεκινάει η καταμέτρηση.')
        else:
            break    
    f = open(filename, 'r')
    header = f.readline()
    mysum = 0
    counter = 0
    for line in f:
        counter += 1 
        if counter >=starting_month and counter <= ending_month: 
            words = line.split(',') #line : 'January,15\n'
            mysum += float(words[1].rstrip('\n'))       
    print('Τα συνολικά έξοδα για το την περίοδο από τον', months[starting_month], 'έως τον', months[ending_month], 'είναι: ', mysum ,'€.')
                  
# Επιλογή 5: Τρέχον μέσος όρος εξόδων:
def curr_avg(filename): #για τους μήνες που δεν έχουν περάσει έχουμε π.χ. 'Ιούνιος, 0\n'
    f = open(filename, 'r')
    heading = f.readline()
    expenses_summed = 0
    counter = 0
    curr_month = datetime.date.today().month
    for line in f:
        counter += 1
        if counter <= curr_month:
            words = line.split(',') #line : 'January,15\n' and words ['January', '15\n']
            expenses_summed += float(words[1]) 
        else: #ξεπερνάω τον μήνα που διανύουμε
            break
    return format(expenses_summed/curr_month, '.2f')

#Επιλογή 6: Τερματισμός
def quit():
    print('Τερματισμός...')

# Η κύρια συνάρτηση
def main():
    while True:
        menu()
        choice = get_choice()
        while choice not in list('123456'):
            print('\nΣφάλμα: μη έγκυρη επιλογή!')
            choice = get_choice()
        if choice == '6':
            quit() 
            break
        else:  
            if choice == '1': 
                directory_name = give_directory_name()
                write_expenses_from_scratch(directory_name)
            elif choice == '2':
                filename = give_pathname()
                add_this_month(filename)
            elif choice == '3':
                filename = give_pathname()
                change_exp(filename)
            elif choice == '4':
                filename = give_pathname()
                sum_of_expenses_for_year(filename)
            elif choice == '5':
                filename = give_pathname()
                curr_avg(filename)

# give_expenses(5,False)
# give_expenses(5,True)   
main()         