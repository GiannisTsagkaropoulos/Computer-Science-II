def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

class WrongSizeError(Exception):
    pass

class Matrix():

    def __init__(self, rows, columns):
        matrix = [[0 for i in range(columns)]for j in range(rows)]
        for i in range(rows):
            for j in range(columns):
                print(f'Ποιο είναι το στοιχείο στη θέση {(i+1,j+1)}: ', end = '' )
                elem = input()
                while not(is_int(elem)):
                    print('Το στοιχείο πρέπει να είναι ακέραιος αριθμός.')
                    print(f'Κάνε πάλι εισαγωγή του στοιχείου στη θέση{(i+1,j+1)}: ', end = '' )
                    elem = input()
                matrix[i][j] = int(elem)    
        self.rows = rows
        self.columns = columns        
        self.matrix = matrix

    def __add__(self, other):
        try:
            if self.rows != other.rows or self.columns != other.columns:
                raise WrongSizeError('Οι πίνακες έχουν διαφορετικές διαστάσεις και δεν γίνεται να γίνει πρόσθεση μεταξύ τους.')  
            else:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.matrix[i][j] += other.matrix[i][j]
        except WrongSizeError as error:
            print(error)  

    def __mul__(self,other):   
        try:
            if self.columns != other.rows:
                raise WrongSizeError('Για να μπορεί να γίνει πολλαπλαπλασιασμός πρέπει το πλήθος των στηλών του πρώτου ορίσματος \
                    -πίνακα να είναι ίδιο με το πλήθος γραμμών του δεύτερου ορίσματος-πίνακα.')  
            else:
                mult = [[0 for i in range(other.columns)] for j in range(self.rows)]
                for i in range(self.rows):
                    for j in range(self.columns):
                        for k in range(self.columns):
                            mult[i][j] += self.matrix[i][k]*other.matrix[k][j]
                self.matrix = mult        
        except WrongSizeError as error:
            print(error)             

    def __str__(self):
        s = ''
        for i in range(self.rows):
            for j in range(self.columns):
                if j== self.columns-1:
                    s += str(self.matrix[i][j]) + '\n'
                else:
                    s += str(self.matrix[i][j]) + '\t'
        return s            
a = Matrix(2,2)
print(a)