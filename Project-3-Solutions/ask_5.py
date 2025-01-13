import os 
import string

def give_file_name():
    name = input('Δώσε το όνομα που επιθυμείς να έχει το αρχείο (με κατάληξη .csv ή .txt): ')
    name.replace(' ','_') # τα κενά τα αντικαθιστώ με κάτω παύλες
    while  not( name.endswith('.txt') or name.endswith('.csv') ):
        name = input('Μη έγκυρη επιλογή ονόματος. Δώσε ξανά όνομα για το αρχείο: ') 
        name.replace(' ','_') 
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

def huffman(string):
    codes = {'a':'0', 'b':'10', 'c':'110', 'd':'111'}
    encoded = ''
    for i in range(len(string)):
        if string[i] in list('abcd'):
            encoded += codes[string[i]]
        else:
            encoded += string[i]
    return encoded

def dict_encoding(string, dictionary):
    encoded = ''
    for ch_index in range(len(string)):
        ch = string[ch_index]
        if ch in dictionary:
            encoded += dictionary[ch]
        else:
            encoded += ch
    return encoded


punct = list(string.punctuation) + ['\n', '\t']

def podana(word): #μπορεί η λέξη να τελειώνει με ., !, ; , ? , (, ), ,, 
    #will reverse the word to remove punctuation from ending with the replace method
    clean = word[::-1] #το τέλος έγινε αρχή
    #clean = word
    #ENDING
    last_char = clean[0]
    end_removed = ''
    while last_char in punct: 
        end_removed += last_char
        clean = clean.replace(last_char,'',1)
        last_char = clean[0]
    end_removed = end_removed[::-1]  #οι χαρακτήρες εξάγονται από έξω προς μέσα (ακόμα και αν αναποδογυριστεί η λέξη) 
    clean = clean[::-1] #η λέξη έχει κανονική μορφή της χωρίς σημεία στήξης δεξία
    #FRONT
    first_char = clean[0]    
    front_removed = ''
    while first_char in punct:
        front_removed += first_char  
        clean = clean.replace(first_char,'',1)
        first_char = clean[0]  
    if len(clean) == 1:
        encoded = clean
    else:
        encoded = clean[(len(clean)//2):] + clean[0:(len(clean)//2)] 
    print(front_removed + encoded + end_removed)  

def podana_encoding(string):
    words = string.split()
    encoded_text = ''#initialization
    for i in len(words):
        encoded = podana(words[i])
        encoded_text += encoded
    return encoded_text    

class Encoded():
    
    def __init__(self, filename, number):
        ###
        try:
            if type(filename) != str and not(filename.endswith('.txt') or filename.endswith('.csv')): # Δεν είναι αρχείο κειμένου
                raise FileNotFoundError('Το αρχείο που εισήγαγες δεν είναι αρχείο κειμένου')
            else:   
                f = open(filename)
        except FileNotFoundError as error: 
            print(error)
            name = give_file_name()
            dir = give_directory_name() 
            filename = dir + '/' + name
        finally:    
            f = open(filename, 'r')
            normal_text = f.read()
            self.__text = normal_text
        ##Κωδικοποίηση
        if number not in [1,2,3]:
            print('Yπάρχουν μόνο 3 επιλογές κωδικοποίησης του αρχείου.')
            print('1. Κωδικοποίηση Huffman.')
            print('2. Κωδικοποίηση βάσει λεξικού')
            print('3. Κωδικοποίηση ποδανά.')
            choice = input('Επίλεξε κωδικοποίηση: ')
            while choice not in list('123'):
                print('Μη έγκυρη επιλογή')
                choice = input('Επίλεξε κωδικοποίηση: ')
            number = int(choice)    
        if number == 1:
            self.__text = huffman(self.__text)
        elif number == 2: #dictionary
            self.__text = dict_encoding(self.__text, dictionary) #το λεξικό είναι προκαθορισμένο
        elif number == 3:
            self.__text = podana_encoding(self.__text)

    def print_file(self):
        print(self.__text)     

    def save_file(self):
        name = give_file_name()
        dir = give_directory_name() 
        filename = dir + '/' + name     
        f = open(filename, 'w')
        f.write(self.__text)
        f.close()