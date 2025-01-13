import random
from locale import LC_ALL
from multiprocessing.connection import wait
import random
import itertools
import threading
import time
import sys 
#INITIALIZATIONS
List = ['πέτρα', 'μολύβι','ψαλίδι','χαρτί']
RED = '\033[31m'
GREEN = '\033[92m'
BLACK = '\033[0m'
BLUE = '\033[94m'

def menu():
    print(RED + '\n-----------------ΜΕΝΟΥ-----------------\n' + BLACK)
    print('1) Πέτρα')
    print('2) Μολύβι')
    print('3) Ψαλίδι')
    print('4) Χαρτί')

#επιστρέφει επιλογή χρήστη (1,2,3,4)  
def get_choice(): 
    choice = input("\nΕπίλεξε μία από τις παραπάνω επιλογές: ")
    while choice not in list('1234'):
        choice = input("Μη έγκυρη επιλογή. Επίλεξε ξανά μία από τις παραπάνω επιλογές: ") 
    return int(choice)

# # For the animation
def animate():
    i = 0
    for c in itertools.cycle(['Πέτρα', 'Μολύβι', 'Ψαλίδι', ' Χαρτί']):
        i+=1
        if i > 4:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.4)    

def main():
    menu()
    user = get_choice() #1,2,3,4   #επιλογή χρήστη
    computer = random.randint(1,4) #1-> πέτρα, 2-> μολύβι, 3-> ψαλίδι, 4->χαρτί   #επιλογή υπολογιστή
    animate()
    while  List[user-1] == List[computer-1]:
        print('\n\nΕπέλεξες', List[user-1],'και ο υπολογιστής έφερε',List[computer-1])
        print(BLUE + '\nΙσοπαλία' + BLACK)
        print('\nHere we go again\n')
        main()
        
    else:   
        winning = [['ψαλίδι','χαρτί'],['ψαλίδι','μολύβι'],['πέτρα','ψαλίδι'],['πέτρα','μολύβι'],['χαρτί','πέτρα'],['μολύβι','χαρτί']]
        if [ List[user-1],List[computer-1] ] in winning:
            print('\n\nΕπέλεξες', List[user-1],'και ο υπολογιστής έφερε', List[computer-1])
            print(GREEN + '\nΚέρδισες!!!' + BLACK)
        else:
            print('\n\nΕπέλεξες', List[user-1],'και ο υπολογιστής έφερε',List[computer-1])
            print(RED + '\nΈχασες :(' + BLACK)   

main()        