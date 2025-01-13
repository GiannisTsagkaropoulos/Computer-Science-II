import string
from types import NoneType

punct = list(string.punctuation) 
tonismena = {'ά':'α', 'έ':'ε', 'ή':'η', 'ί':'ι', 'ό':'ο', 'ύ':'υ', 'ώ':'ω', 'σ':'ς'}# 'ς':'σ'}
tonismena_reverse =  {'α':'ά', 'ε':'έ', 'η':'ή', 'ι':'ί', 'ο':'ό', 'υ':'ύ', 'ω':'ώ', 'ς':'σ'}

def is_word(word):
    if type(word) == str:
            word = word.rstrip('\n')
            word = word.rstrip('\t')
            while word[len(word)-1] in punct:
                word = word[:-1]
            if len(word)<2 or not(word.isalpha()):
                print('Μη αποδεκτή λέξη για κρεμάλα.')
                return None
            else:
                return word       
    else:
        print('Πρέπει να εισάγετε λέξη τύπου str.')   
        return None   
         
def give_letter():
    letter = input('Δώσε γράμμα: ')
    while len(letter) > 1 or not(letter.isalpha()):
        letter = input('Μη έγκυρη επιλογή. Δώσε ξανά γράμμα: ')
    return letter.lower() #είναι μικρό 

class Game():
    
    def __init__(self, word):
        word = is_word(word)
        while type(word) == NoneType:
            word = input('Παρακαλώ εισάγετε καινούρια λέξη: ')
            word = is_word(word)            
        # print(word)    
        self.__word = word #είναι τονισμένη και μπορεί να έχει τελικός
        self.__fails = 0
        self.__spaces = list(range( len(word) ))
        self.__letters = []

    def show_word(self):
        guess = ''
        for i in range( len(self.__word) ):
            if i in self.__spaces:
                guess += '_'  
            else:
                guess +=  self.__word[i]    
        print('Η λέξη είναι η: ', guess)

    def next_round(self): 
        letter = give_letter()
        while (letter in tonismena and tonismena[letter] in self.__letters) or (letter in tonismena_reverse) and (tonismena_reverse[letter] in self.__letters):
            print('Το έχεις ξαναδώσει αυτό το γράμμα.\n')
            letter = give_letter()
        else:
            while letter in self.__letters:
                print('Το έχεις ξαναδώσει αυτό το γράμμα.\n')
                letter = give_letter()
        (self.__letters).append(letter)  
        ##έχει δωθεί το γράμμα το οποίο μπορεί να είναι και τονισμένο ή και να είναι το τελικό σ
        index = [] #initialization
        if letter in tonismena and (letter in  self.__word or tonismena[letter] in self.__word): #τονισμένο φωνήεν, έλεγχος αν αυτό ή το φωνήεν χωρίς τόνο βρίσκεται στη λέξη.
            for i in range(len(self.__word)):
                if self.__word[i] == letter or self.__word[i] == tonismena[letter]:
                    index.append(i)
        elif letter in tonismena_reverse and (letter in  self.__word or tonismena_reverse[letter] in self.__word): #άτονο φωνήεν(ή ς), έλεγχος αν αυτό ή το φωνήεν με τόνο(ή το σ) βρίσκεται στη λέξη.                
            for i in range(len(self.__word)):
                if self.__word[i] == letter or self.__word[i] == tonismena_reverse[letter]:
                    index.append(i)   
        elif letter not in tonismena and letter  not in tonismena_reverse:
            for i in range(len(self.__word)):
                if self.__word[i] == letter:
                    index.append(i)             
        return index            

    def evaluate(self):
            indices = self.next_round()
            if indices ==  []:
                self.__fails += 1
            else:
                for i in indices:
                    self.__spaces.remove(i)   

    def play(self):
        while self.__fails < 6:
            self.show_word()
            if self.__spaces == []:
                print('\n !!!YOU WON!!!')
                break
            if self.__letters == []:
                print('Έχεις 6 δυνατότητες να αποτύχεις και δεν έχεις επιλέξει ακόμα γράμματα.')
            else: 
            
                print(f'\n Έχεις {6-self.__fails} δυνατότητες να αποτύχεις.\n')
                print('Μέχρι στιγμής έχεις επιλέξει τα γράμματα: ', self.__letters, '\n')
            self.evaluate()      
        else:
            print('\n GAME OVER.')  
            print('\n Η λέξη ήταν : ', self.__word)    

a = Game('άρρωστος')
a.play()