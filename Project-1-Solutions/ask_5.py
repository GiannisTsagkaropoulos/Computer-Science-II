RED = '\033[31m'
GREEN = '\033[92m'
BLACK = '\033[0m'
BLUE = '\033[94m'

def str_to_dig(coord):
    coord[0] = ord(coord[0].lower())-96 # a->97, b->98 , c->99 και τα κάνω a->1, b->2, c->3 ...
    coord[1] = int(coord[1])
    return coord

def coords_are_valid(coords_of_all):
    if coords_of_all[0] in coords_of_all[1:] or coords_of_all[1] == coords_of_all[2]:
        print(RED + '\nΈχεις τοποθετήσει 2 πιόνια στην ίδια θέση.' +BLACK)
        print('Here we go again')
        give_coordinates()

def give_coordinates():
    print(BLUE + '\n------------Είσοδος συντεταγμένων------------\n' + BLACK)
    pionia = ['black king','white king','white queen']
    coords_of_all = []
    for i in pionia: 
        print('Give coordinates of',i ,':', end ='')
        coord = list(input())
        while len(coord) != 2:
                print('Not valid entry2. Give coordinates of ',i,' again:', end ='')
                coord = list(input())
        else:
            if coord[0].lower() not in list('abcdefgh') or coord[1] not in list('12345678') :   
                print('Not valid entry2. Give coordinates of ',i,' again:', end ='')    
                coord = list(input())            
        coords_of_all.append(str_to_dig(coord))
    coords_are_valid(coords_of_all)
    return coords_of_all    

def king_next_moves(coord, wq_pos): #coord = ['n','k'] with n,k in {1,2,3,4,5,6,7,8}
    x2,y2 = coord[0], coord[1]
    global aroundblock, removecounter
    removecounter = 0 #initialization
    aroundblock = [[x2+1,y2-1],[x2+1,y2],[x2+1,y2+1],[x2,y2-1],[x2,y2+1],[x2-1,y2-1],[x2-1,y2],[x2-1,y2+1]]
    for i in range(len(aroundblock)):
        if 0 in aroundblock[i-removecounter] or 9 in aroundblock[i-removecounter]: #out of range
            del aroundblock[i-removecounter]
            removecounter +=1
        if i+removecounter == 7: #αν δεν είχαμε αφαιρέσει στοιχεία το i θα έτρεχε μέχρι 7
            break
    if wq_pos in aroundblock: 
        aroundblock.remove(wq_pos)
    return aroundblock

def queen_next_moves(white_king_coords, white_queen_coords): #δέχεται θέσεις άσπρου βασιλία και βασίλισσας για
    #να ελέγξει αν η βασίλισσα όπως κινείται θα "πέσει" πάνω στον άσπρο βασιλιά
    qn = [ [], [], [], [] ] #initialization
    x1 , y1 = white_king_coords[0], white_king_coords[1]
    x2 , y2 = white_queen_coords[0], white_queen_coords[1]
    for i in range(1,9): # i = 1,2,3,4,5,6,7,8
        #ΚΑΤΑΚΟΡΥΦΕΣ
        if i!=y2: #για να μη βάλω και θέση βασίλισσας μέσα
            if x1 != x2: #white king, white queen όχι στην ίδια κατακόρυφη
                qn[0].append([x2,i])
            else: 
                if x1+y1 < x2+y2 and i >= y1: #ο βασιλιάς πιο χαμηλά από βασίλισσα άρα εμποδίζει θέσεις από κάτω
                    qn[0].append([x2,i]) 
                elif x1+y1 > x2+y2 and i <= y1: #ο βασιλιάς πιο ψηλά από βασίλισσα άρα εμποδίζει θέσεις από πάνω
                    qn[0].append([x2,i])   
        #ΟΡΙΖΟΝΤΙΕΣ
        if i!=x2: #για να μη βάλω και θέση βασίλισσας μέσα
            if y1 != y2: #white king, white queen όχι στην ίδια κατακόρυφη
                qn[1].append([i,y2])
            else: 
                if x1+y1 < x2+y2 and i >= y1: #ο βασιλιάς πιο αριστερά από βασίλισσα άρα εμποδίζει θέσεις από αριστερά
                    qn[0].append([i,y2]) 
                elif x1+y1 > x2+y2 and i <= y1: #ο βασιλιάς πιο δεξιά από βασίλισσα άρα εμποδίζει θέσεις από δεξιά
                    qn[1].append([i,y2])     
##############################################################################################################                    
    ###Πλάγιες δεξιές
        if i <= (8-abs(x2-y2)): #η οριζόντια απόσταση βασίλισσας από θέση που ανήκει σε κύρια διαγώνιο που
            #υποδεικνύει πόσα πλάγια δεξιά βήματα μπορεί να κάνει 
            if x2-y2 >=0: #κάτω από κύρια διαγώνιο (i=j)
                if x1-y1 != x2-y2: #οι διαφορές είναι σταθερές κινούμενοι πλάγια δεξιά. Αν είναι διαφορετικές,
                                    # βασιλιάς δεν εμποδίζει κίνηση βασίλισσας πλάγια δεξιά
                    qn[2].append([x2-y2+i,i])
                else: #βασιλιάς εμποδίζει κίνηση βασίλισσας πλάγια δεξιά
                    if  x1+y1 < x2+y2 and i >= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[2].append([x2-y2+i,i])
                    elif  x1+y1 > x2+y2 and i <= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[2].append([x2-y2+i,i])        
            else: #πάνω από κύρια διαγώνιο (i=j)
                if x1-y1 != x2-y2: #οι διαφορές είναι σταθερές κινούμενοι πλάγια δεξιά. Αν είναι διαφορετικές,
                                    # βασιλιάς δεν εμποδίζει κίνηση βασίλισσας πλάγια δεξιά
                    qn[2].append([i,abs(x2-y2)+i])
                else: #βασιλιάς εμποδίζει κίνηση βασίλισσας πλάγια δεξιά
                    if  x1+y1 < x2+y2 and i >= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[2].append([i,abs(x2-y2)+i])
                    elif  x1+y1 > x2+y2 and i <= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[2].append([i,abs(x2-y2)+i])  
        #####Πλάγιες αριστερές
        #ορίζω δευτερεύουσα διαγώνιο αυτή που ξεκινάει από πάνω δεξιά θέση και καταλήγει σε κάτω
        if i<=(8-abs(9-(x2+y2))):#η οριζόντια απόσταση βασίλισσας από θέση που ανήκει σε δευτερεύουσα διαγώνιο.
            # που αν αφαιρεθεί από το 8 υποδεικνύει πόσα πλάγια αριστερά βήματα μπορεί να κάνει 
            if x2+y2<=9: # κάτω από δευτερεύουσα διαγώνιο
                if x1+y1 != x2+y2: #τα αθροίσματα είναι σταθερά κινούμενοι πλάγια αριστερά. Αν είναι διαφορετικά,
                                    # βασιλιάς δεν εμποδίζει κίνηση βασίλισσας πλάγια αριστερά
                    qn[3].append([i,x2+y2-i])
                else: #βασιλιάς εμποδίζει κίνηση βασίλισσας πλάγια αριστερά
                    if x1-y1 < x2-y2 and i >= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[3].append([i,x2+y2-i])
                    elif x1-y1 > x2-y2 and i <= x1:
                        qn[3].append([i,x2+y2-i])
        ###############
            else: #πάνω από δευτερεύουσα διαγώνιο
                if x1+y1 != x2+y2: #αθροίσματα διαφορετικά άρα δεν ανήκουν στην ίδια πλάγια αριστερή
                    qn[3].append([x2+y2-9+i,9-i])
                else:  #αθροίσματα ίδια άρα ανήκουν στην ίδια πλάγια αριστερή  
                    if x1-y1 < x2-y2 and i >= x1:  #βασιλιάς πιο κάτω (δεξιά κινούμενοι) από βασίλισσα
                        qn[3].append([x2+y2-9+i,9-i])
                    elif x1-y1 > x2-y2 and i <= x1:
                        qn[3].append([x2+y2-9+i,9-i])
    for j in range(2,4):
        if white_queen_coords in qn[j]:
            qn[j].remove(white_queen_coords)
    #qn is [[],[],[],[]]]
    qnext = []
    for i in range(4):
        for j in qn[i]:
            qnext.append(j)
    return qnext    


def showchessboard():
    for i in range(1,9):
        print(i, end = '        \n')
    print('A B C D E F G H')     


def ruamat_or_rua(bk_next_moves,black_king_pos,queen_next,wk_next_moves):
    apeilh = queen_next + wk_next_moves
    counter = 0
    R = 0
    for i in bk_next_moves:
        if black_king_pos in apeilh and  i in apeilh  :
            counter += 1 
    flag = True
    if counter == len(bk_next_moves):
        print(RED+ '\n ----Ρουα ματ----\n'+BLACK)
        R = 1
        flag = False
    if (black_king_pos in queen_next or black_king_pos in wk_next_moves) and flag:
        print(RED+ '\n -----Ρουα-----\n'+BLACK)
    return R

def main():
    coords_of_all = give_coordinates() #αφού κάνει ελέγχους επιστρέφει λίστα με τις 3 συντεταγμένες σε 
    #μορφή :[1,2] με σειρά black king, white king, white queen
    black_king_pos = coords_of_all[0]
    wk_pos = coords_of_all[1]
    wq_pos = coords_of_all[2]
    bk_next_moves = king_next_moves( black_king_pos, wq_pos ) #έχουμε δυνατές επόμενες κινήσεις άσπρου βασιλιά
    if coords_of_all[1] in bk_next_moves:
        print(RED + 'Δεν μπορούν οι βασιλιάδες να απέχουν 1 βήμα απόσταση'+BLACK)
        print('Here we go again')
        give_coordinates()
    wk_next_moves = king_next_moves( coords_of_all[1], [0,0] ) #έχουμε δυνατές επόμενες κινήσεις άσπρου βασιλιά
    queen_next = queen_next_moves(coords_of_all[1], coords_of_all[2])
    R = ruamat_or_rua(bk_next_moves,black_king_pos,queen_next,wk_next_moves)
    chessBoard(black_king_pos,wk_pos,wq_pos,R)

   
def chessBoard(th1,th2,th3,R = 0):
    for i in range(8,0,-1):
        if i%2 != 0:
            print(i,end='|')
            for j in range(1,9):
                if j%2 != 0:
                    if i == int(th1[1]) and j == int(th1[0]) and R == 0:
                        print('\033[48;5;239m\033[38;5;232m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th2[1]) and j == int(th2[0]):
                        print('\033[48;5;239m\033[38;5;231m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th3[1]) and j == int(th3[0]):
                        print('\033[48;5;239m\033[38;5;231m🅠 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th1[1]) and j == int(th1[0]) and R == 1 :
                        print('\033[48;5;239m\033[38;5;196m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    print('\033[48;5;239m\033[38;5;232m  \033[0;0m',end = '')
                    if j == 8:
                        print(end='\n')
                else:
                    if i == int(th1[1]) and j == int(th1[0]) and R == 0:
                        print('\033[48;5;247m\033[38;5;232m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th2[1]) and j == int(th2[0]):
                        print('\033[48;5;247m\033[38;5;231m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th3[1]) and j == int(th3[0]):
                        print('\033[48;5;247m\033[38;5;231m🅠 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th1[1]) and j == int(th1[0]) and R == 1 :
                        print('\033[48;5;247m\033[38;5;196m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    print('\033[48;5;247m\033[38;5;232m  \033[0;0m',end = '')
                    if j == 8:
                        print(end='\n')
        else:
            print(i,end='|')
            for j in range(1,9):    
                if j%2 != 0:
                    if i == int(th1[1]) and j == int(th1[0]) and R == 0:
                        print('\033[48;5;247m\033[38;5;232m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th2[1]) and j == int(th2[0]):
                        print('\033[48;5;247m\033[38;5;231m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th3[1]) and j == int(th3[0]):
                        print('\033[48;5;247m\033[38;5;231m🅠 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th1[1]) and j == int(th1[0]) and R == 1 :
                        print('\033[48;5;247m\033[38;5;196m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    print('\033[48;5;247m\033[38;5;232m  \033[0;0m',end = '')
                    if j == 8:
                        print(end='\n')
                else:
                    if i == int(th1[1]) and j == int(th1[0]) and R == 0:
                        print('\033[48;5;239m\033[38;5;232m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th2[1]) and j == int(th2[0]):
                        print('\033[48;5;239m\033[38;5;231m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th3[1]) and j == int(th3[0]):
                        print('\033[48;5;239m\033[38;5;231m🅠 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    if i == int(th1[1]) and j == int(th1[0]) and R == 1:
                        print('\033[48;5;239m\033[38;5;196m🅚 \033[0;0m',end = '')
                        if j == 8:
                            print(end='\n')
                        continue
                    print('\033[48;5;239m\033[38;5;232m  \033[0;0m',end = '')
                    if j == 8:
                        print(end='\n')
    print('  𝓐 𝓑 𝓒 𝓓 𝓔 𝓕 𝓖 𝓗')

main() 