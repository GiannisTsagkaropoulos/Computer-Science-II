from locale import LC_ALL
from multiprocessing.connection import wait
import random
import itertools
import threading
import time
import sys 

#Initializations
RUL = [('πράσινο',[0]),('κόκκινο',[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]) \
    ,('μαύρο',[2,4,6,8,10,11,13,15,17,20,22,24,26,28,31,33,35])] #initialization
L = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36'
L = L.split(',')
RED = '\033[31m'
GREEN = '\033[92m'
BLACK = '\033[0m'

# Το μενού
def menu():
    print(RED + '\n---------------------ΜΕΝΟΥ-----------------------\n' + BLACK)
    print('1) Αριθμός (0 έως 36), κέρδος 35m μάρκες')
    print('2) Χρώμα ('+ RED + 'Κόκκινο' +BLACK + '/Μαύρο), κέρδος m μάρκες')
    print('3) Μονά / Ζυγά, κέρδος m μάρκες\n\n')

# string_n είναι φυσικός ή όχι;
def check_Natural_Number(string_n):
    if str(string_n).isdigit() and (float(string_n) == int(string_n) and int(string_n) > 0):
        return True
    else:
        return False

#Επιλογή χρήστη για ποντάρισμα
def get_choice(reset_posoy,poso): #επιστρέφει λίστα με int τα [επιλογή πονταρίσματος, ποντάρισμα, ποσό από μάρκες που έχω]
    global choice, m, list_with_all
    ######################################################################
    if reset_posoy == True:   
        poso = input('Πόσες μάρκες διαθέτεις; ') 
        while not(check_Natural_Number(poso)): #while poso όχι φυσικός αριθμός
            input('Μη έγκυρη επιλογή πονταρίσματος. Δώσε ξανά ποσό που ποντάρεις σε μάρκες:')      
    else:     
        print('Συνεχίζεις το παιχνίδι με ',poso, 'μάρκες') 
    choice = input('Δώσε την επιλογή για τρόπο πονταρίσματος (1,2 ή 3): ')
    while choice not in list('123'):
        choice = input('Μη έγκυρη επιλογή τρόπου πονταρίσματος. Δώσε ξανά την επιλογή σου (1,2 ή 3): ')
    #θέλουμε, αν ξαναπαίζουμε, να διατηρούμε το ποσό μαρκών
    #    
    m = input('Δώσε ποσό που ποντάρεις σε μάρκες: ')     
    while not(check_Natural_Number(m)):  #while m όχι φυσικός αριθμός
        m = input('Μη έγκυρη επιλογή πονταρίσματος. Δώσε ξανά ποσό που ποντάρεις σε μάρκες:') 
    #    
    choice, m, poso = int(choice), int(m), int(poso)     
    #
    while m > poso:
        print(RED+'\nΔε γίνεται να ποντάρεις περισσότερες μάρκες από όσες διαθέτεις.\n'+ BLACK + \
            'Eισαγωγή δεδομέων από την αρχή\n ------------------------------------------------') 
        # menu()    
        # get_choice() 
        main(poso,reset_posoy)
    list_with_all =  [choice,m,poso]  #είναι όλα integers     
    return   list_with_all

# rulete loading
def loading():
    t = threading.Thread(target=animate)
    t.start()
    start = time.time()
    while time.time() - start < 2:
        wait

# Ρίξιμο κρουπιέρη
def roulete_number():
    loading()
    x = random.randint(0,36)
    return x

# Επιλογή αριθμού στο [0,36] από χρήστη
def give_number():
    x = input('\nΔιάλεξε έναν ακέραιο αριθμό από το 0 έως και το 36: ')
    while x not in L: # x not natural number OR not in [0,36] 
        x = input('Μη έγκυρη επιλογή αριθμού. Διάλεξε έναν ακέραιο αριθμό από το 0 έως και το 36: ')
    return int(x)

# Επιλογή χρώματος από χρήστη  
def give_colour():
    colour = input('\nΕπίλεξε χρώμα (Κόκκινο/Μαύρο): ')
    colours = ['red','κόκκινο','κοκκινο','kokkino','black','μαύρο','μαυρο','mauro','mayro']
    while colour.lower() not in  colours:
        colour = input('Μη έγκυρη επιλογή χρώματος. Επίλεξε ξανά χρώμα (Κόκκινο/Μαύρο): ')
    if colours.index(colour) <= 3: #χρώμα 'κόκκινο'. Στη RUL έτσι είναι τα χρώματα
        colour = 'κόκκινο'
    else:
        colour = 'μαύρο'        
    return colour  

#επιλογή χρήστη για μονά ή ζυγά
def give_mona_zyga():
    epilogi = input('\n Μονά ή ζυγά; ')
    epiloges = ['μονά','μονα','mona','zyga','ziga','ζυγά','ζυγα']
    while  epilogi.lower() not in epiloges:
        epilogi = input('Μη έγκυρη επιλογή. Μονά ή ζυγά; ')
    if epiloges.index(epilogi) <=2: 
        epilogi = 'μονός' 
    else:
        epilogi = 'ζυγός'       
    return epilogi
    
# Επιλογή 1
def ena(m,poso):
    y = poso
    x = give_number() 
    input('\n Πάτα enter για να ρίξει ο κρουπιέρης')
    chosen =  roulete_number() # θα κάνει animation και το chosen θα πάρει τιμή int αριθμού in [0,36]
    print('\n Ήρθε ο αριθμός ',chosen)
    if x != chosen:  #ο αριθμός που επιλέξαμε διαφορετικός από αυτόν που ήρθε
        print('\nΗ μπάλα έπεσε στον αριθμό: ', chosen,' ενώ εσύ επέλεξες τον αριθμό', x, RED +'\nΈχασες!\n' + BLACK)
        y -= m
        print('Το ποσό μαρκών που διαθέτεις είναι ', y,'.\n')
    else:  #ο αριθμός που επιλέξαμε ίδιος με αυτόν που ήρθε
        print('\nΗ μπάλα έπεσε στον αριθμό: ', chosen, GREEN + '\n Μόλις κέρδισες ', 35*m ,'μάρκες\n!!!' + BLACK)    
        y += 35*m
        print('Το ποσό μαρκών που διαθέτεις είναι ', y,'.\n')
    return y 

# Επιλογή 2
def dyo(m,poso):
    y = poso
    my_colour = give_colour()
    input('\n Πάτα enter για να ρίξει ο κρουπιέρης')
    x = roulete_number() #η μπάλα πέφτει σε αριθμό. Όχι σε χρώμα
    for tup in RUL: #tup είναι λίστα με χρώμα και όλους τους αριθμούς με αυτό το χρώμα π.χ ('πράσινο',[0])
        if x in tup[1]: # x θα πάρει σαν τιμή το χρώμα που έχει ο αριθμός που ήρθε (δηλαδή το x) 
            x = tup[0]
            break #δεν πρόκειται να υπάρξει ο αριθμός με άλλο χρώμα
    if  x != my_colour: #το χρώμα που επιλέξαμε είναι διαφορετικό από αυτό που ήρθε
        print('\nΗ μπάλα έπεσε στο χρώμα: ', x,'ενώ εσύ είχες επιλέξει', my_colour, RED + '\nΈχασες\n' + BLACK)
        y -= m
        print('Το ποσό μαρκών που διαθέτεις είναι ', y,'.\n') 
    else: #το χρώμα που επιλέξαμε είναι ίδιο με αυτό που ήρθε
        print('\nΗ μπάλα έπεσε στο χρώμα: ', x, GREEN + '\n Μόλις κέρδισες ', m,'μάρκες!!!\n' + BLACK) 
        y += m
        print('Το ποσό μαρκών που διαθέτεις είναι ', y,'.\n')
    return y

#Επιλογή 3  
def tria(m,poso):
    w = poso
    my_x = give_mona_zyga() # Επιλογή χρήστη με έξοδο: 'μονός' ή 'ζυγός'
    input('\n Πάτα enter για να ρίξει ο κρουπιέρης')
    x = roulete_number() #η μπάλα πέφτει σε αριθμό και θα εξετάσουμε αν είναι ζυγός ή μονός
    y = x #αντίγραφο του x
    if x%2 == 0: #x άρτιος(ζυγός)
        x = 'ζυγός'
    else:
        x = 'μονός'
    if my_x != x: #lost
        print('\nΗ μπάλα έπεσε στον αριθμό: ', y, ', ο οποίος είναι: ', x,\
            'ενώ εσύ είχες επιλέξει ', my_x, RED+ '\nΈχασες\n' +BLACK ) 
        w -= m
        print('Το ποσό μαρκών που διαθέτεις είναι ', w,'.\n')                 
    else:  #won
        print('\nΗ μπάλα έπεσε στον αριθμό: ', y, ', ο οποίος είναι: ', x, GREEN + '\n Μόλις κέρδισες ',\
             m,'μάρκες!!!\n' + BLACK)  
        w += m
        print('Το ποσό μαρκών που διαθέτεις είναι ', w,'.\n')  
    return w       

# For the animation
def animate():
    start = time.time()
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if time.time() - start > 2:
            break
        sys.stdout.write('\r Γυρνάει η μπάλα ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

def yes_no_answer(ans): #yes = True , no = False
    epiloges = ['ναι','yes','y','όχι','οχι','no']
    if epiloges.index(ans) <=2:
        ans = True
    else:
        ans = False  
    return ans

def want_play_again():
    PLAY_AGAIN = input ('Θες να ξαναπαίξεις (Ναι/Όχι): ')  
    epiloges = ['ναι','yes','y','όχι','οχι','no']
    while PLAY_AGAIN.lower() not in epiloges:
        PLAY_AGAIN = input('Μη έγκυρη επιλογή. Θες να ξαναπαίξεις (Ναι/Όχι): ') 
    answer = yes_no_answer(PLAY_AGAIN)     
    return answer #αν PLAY_AGAIN =  yes τότε answer θα πάρει την τιμή True

def continue_playing(PLAY_AGAIN,poso):
    while PLAY_AGAIN == True and poso >= 0:
        reset_posoy = False #θα συνεχίσει το παιχνίδι άρα δεν θα ξαναεισάγει τις μάρκες που έχει
        if poso == 0:
            print(RED + 'Δυστυχώς δεν έχεις άλλες μάρκες. Για να παίξεις χρειάζεται να δανειστείς.' + BLACK)
            borrow = input('Θες να δανειστείς; (Ναι, Όχι)')
            epiloges = ['ναι','yes','y','όχι','οχι','no']
            while borrow.lower() not in epiloges:
                borrow = input('Μη έγκυρη επιλογή. Θες να δανειστείς (Ναι/Όχι): ')
            borrow = yes_no_answer(borrow)    
            if borrow: #borrow = True άρα θέλει να δανειστεί
                poso = input('Κάνε εισαγωγή του ποσού μαρκών που θες να δανειστείς: ') 
                while not( check_Natural_Number(poso) ):
                    poso = input('Μη έγκυρη επιλογή. Κάνε ξανά εισαγωγή του ποσού μαρκών που θες να δανειστείς: ')
                poso = int(poso) 
                main(poso,reset_posoy) ##################### 
            else:
                print('\nGAME OVER\n',RED+ '\n Είσαι φλώρος και αποχώρησες με',poso, 'μάρκες.')    
        else:          
            main(poso,reset_posoy) 
            # PLAY_AGAIN = want_play_again() 
        return [reset_posoy, poso]    #$$$$$$$$$$$$$
    else: #Play_again == false άρα δεν θέλει να ξαναπαίξει
        print('\nGAME OVER\n',RED+ '\n Είσαι φλώρος και αποχώρησες με',poso, 'μάρκες.')              

# Η κύρια συνάρτηση
def main(poso,reset_posoy):
    menu()
    choice_m_poso = get_choice(reset_posoy, poso) #[τρόπος πονταρίσματος, μάρκες, μάρκες που έχω]
    if choice_m_poso[0] == 1:    #1ος τρόπος πονταρίσματος
        poso = ena(choice_m_poso[1],choice_m_poso[2]) #εκτπώνει λειτουργίες 1 και επιστρέφει ποσό μαρκών
    if choice_m_poso == 2:              #2ος τρόπος πονταρίσματος
        poso = dyo(choice_m_poso[1],choice_m_poso[2])
    elif choice_m_poso == 3:            #3ος τρόπος πονταρίσματος
        poso = tria(choice_m_poso[1],choice_m_poso[2])
    PLAY_AGAIN = want_play_again()   
    poso_reset = continue_playing(PLAY_AGAIN,poso) #[reset_poso, poso]
     


reset_posoy = True
PLAY_AGAIN = True   
poso = 0
main(poso,reset_posoy)