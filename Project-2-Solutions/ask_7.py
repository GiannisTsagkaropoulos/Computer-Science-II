import string
punct = list(string.punctuation) + ['\n', '\t']

def encode(word): #μπορεί η λέξη να τελειώνει με ., !, ; , ? , (, ), ,, 
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

def podana(filename):
    f = open(filename,'r')
    encoded_text = ''
    text = f.readlines()
    for line in text:
        words = line.split()
        for i in len(words):
            encoded = encode(words[i])
            encoded_text += encoded
    f.close()
    #
    answer = input('Θες να κρατήσεις το αρχικό κείμενο(Αν απαντήσεις αρνητικά το κείμενο \
    θα χαθεί και θα πάρει τη θέση του το κωδικοποιημένο)')    
    acceptable = ['yes','yy','y','ναι','nai','yup','ya','no','nope','όχι','οχι','oxi']
    while answer.lower() not in acceptable :
        answer = input('Μη έγκυρη απάντηση. Επίλεξε ξανά: ')
    #        
    if acceptable.index(answer) <=  6: #κρατάει αρχικό κείμενο άρα θα δημιουργήσουμε άλλο στο ίδιο path με το κωδικοποιημένο
        path_name = filename.lstrip('/') #Users/giannistsagaropoulos/Desktop/text.txt
        path_name_list = path_name.split('/') # ['Users', 'giannistsagaropoulos', 'Desktop', 'text.txt']
        last = path_name_list.pop(-1) #'text.txt'
        last = last.split('.') # ['text', 'txt']
        new_name = last[0] + '_copy' + last[1] #'text_copy.txt'
        path_name_list = path_name_list[:-1] + [new_name] # ['Users', 'giannistsagaropoulos', 'Desktop', 'text_copy.txt']
        newfilename = ''
        for i in path_name_list:
            newfilename+= '/'+i
        input ('Πάτα enter για δημιουργία νέου αρχείου με το κωδικοποιημένο αρχικό αρχείο')    
        f = open(newfilename,'w')
        f.write(encoded_text)
        f.close()
    else: #δεν κρατάμε το αρχικό 
        f = open(filename,'w')
        f.write(encoded_text)       