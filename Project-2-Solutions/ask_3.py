def product(A,x):
    sum = 0
    prev_row = sorted(A)[0][0] #γραμμή 1ου !=0 στοιχείου, για αποφυγή Name Error στην 1η επανάληψη στο curr-prev
    prod = {}
    for tup in A: #είναι sorted κατά συντεταγμένες από υπόθεση
        curr_row = tup[0]
        diff = curr_row - prev_row
        if diff == 0: #συνεχίζω να βρίσκομαι στην ίδια γραμμή
            try:
                sum += A[tup]*x[(tup[1],1)] 
            except KeyError: #x[(tup[1],1)]==0 άρα δεν υπάρχει  x[(tup[1],1)]
                continue    
        else: #curr_row - prev_row =1 --> άλλαξα γραμμή
            if sum !=0: #αλλιώς δεν το θέλω σαν στοιχείο
                prod[(prev_row,1)] = sum #εισαγωγή στοιχείου
            sum = 0 #αρχικοποίηση και ξεκινάει δουλειά για τη νέα γραμμή
            try:
                sum += A[tup]*x[(tup[1],1)] 
            except KeyError:
                continue    
        prev_row = curr_row
    if sum!=0: #τελευταία γραμμή που έλεγξα (#αν είναι 0, δεν το θέλω σαν στοιχείο)
        prod[(prev_row,1)] = sum        
    return prod

# A ={(1,1):1, (1,2):2, (1,3):3, (2,1):1, (2,4):5, (3,2):7, (3,4):9}    
# x = {(1,1):2, (4,1):1}
# product(A,x)