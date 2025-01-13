from re import A
import time

def menu():
    print('\n-------------------\n       Μενού\n-------------------')
    print('α) Προσθήκη στοιχείου στην ουρά προτεραιότητας')
    print('β) Επιστροφή ονόματος που πρέπει να εξυπηρετηθεί πρώτα')
    print('γ) Τερματισμός\n')

def get_choice():
    choice = input('Επίλεξε α ή β ή γ:')
    alist = ['a','α','a)','α)']
    blist = ['b','β','b)','β)']
    clist = ['c','γ','c)','γ)']
    while choice.lower() not in alist+blist+clist:
        choice = input('Μη έγκυρη επιλογή. Επίλεξε α ή β ή γ:')
    if choice.lower() in alist:
        choice = 'a'
    elif choice.lower() in blist: 
        choice = 'b'      
    elif choice.lower() in clist:
        choice = 'c'    
    return choice    

def a():
    name = input('Δώσε όνομα:')
    while not(name.isalpha()):
        name = input('Μη έγκυρη επιλογή. Δώσε ξανά όνομα:')
    prior = input('Δώσε προτεραιότητα:')
    while not(prior.isdigit()):
        prior = input('Μη έγκυρη επιλογή. Δώσε ξανά προτεραιότητα:')           
    time1 = time.time()
    value = {'name': name,'priority': prior}
    return time1,value

def b(dic):
    try: 
        low_time = list(dic.keys())[0] #αρχικοποίηση time (1ο key)
        low_prior = dic [low_time]['priority'] #αρχικοποίηση priority, 1ou key
        for key in dic:
            if dic[key]['priority'] <= low_prior and key < low_time :
                low_prior, low_time = dic[key]['priority'], low_time
            #low time είναι το κλειδί-χρόνος με τη μικρότερη προτεραιότητα 
        next = dic[low_time] #{'name':..., 'priority': ...}
        name = next['name']
        output = 'Πρέπει να εξυπηρετηθεί πρώτα ο/η' + name
        del dic[low_time]
    except (IndexError, KeyError):
        output = 'Η ουρά προτεραιότητας είναι κενή'         
    return output, dic

def main():
    while True:    
        menu()
        choice = get_choice() #a or b or c
        if choice == 'a': 
            tup = a() #(time, {'name': .. , 'priority': 2})
            try:
               my_dict[tup[0]] = tup[1]  
            except NameError: #δημιουργία λεξικού αν δεν υπάρχει
                my_dict = {}
                my_dict[tup[0]] = tup[1]   
        elif choice == 'b':
            try:
                tupl = b(my_dict) #(output, my_dict renewed(without the removed key))
                print(tupl[0],'\n')
                my_dict = tupl[1] 
            except  UnboundLocalError:
                print('\nΔεν υπάρχει ουρά προτεραιότητας')     
        elif choice == 'c':    
            print('Τερματισμός...')
            break

c = {12:{'name':'alex', 'priority':7}, 13:{'name':'aex', 'priority':6}, 5:{'name':'aey', 'priority':8}, 9:{'name':'picki', 'priority':8}}
main()