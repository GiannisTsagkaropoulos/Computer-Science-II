def menu():
    temperatures = ['(1) Fahrenheit | F = C*9/5+32','(2) Kelvin | K = C+273.15','(3) Rankive | R = C+273.15*9/5'\
    ,'(4) Delisle | Dc = (100 -C)*3/2','(5) Newton | N = C - 33/100 ','(6) Reamur | Re = C*4/5','(7) Rømer | Ro = C*21/40+7.5']
    row = len(temperatures[0])
    for i in temperatures:
        if len(i) >= row:
            row = len(i)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    for j in temperatures:
        x = (row - len(j))*' '
        result= h + '\n'"|"+j+x+"|"'\n' + h
        print(result)
# menu()

def convert(temp,choice):
    converter = [temp*1.8 +32,temp+273.15,temp+491.67,(100 -temp)*1.5,temp - 0.33,temp*0.8,temp*0.525+7.5]
    return round(converter[choice-1],2)

def main():
    temperatures = ['Fahrenheit','Kelvin','Rankive','Delisle','Newton','Reamur','Rømer']
    menu()
    temp = is_number()
    while temp == 'λάθος':
        print('Μη έκγυρη επιλογή. Διάλεξε ξανά τη θερμοκρασία σε βαθμούς Κελσίου: ')
        temp = is_number()
    temp = float(temp)    
    choice = input('Διάλεξε τη μετατροπή που θες από τον πίνακα (1 ,2,..., 7): ')
    while choice not in list('1234567'):
        choice = input('Μη έκγυρη επιλογή. Διάλεξε ξανά τη μετατροπή που θες από τον πίνακα (1 ,2,..., 7): ')
    choice = int(choice)
    converted = convert(temp,choice)
    print('Η θερμοκρασία που διάλεξες ειναι \033[2;31m {}°C \033[0;0m'.format(temp))
    print('Και η θερμοκρασία σε %s είναι \033[2;31m %s \033[0;0m'%(temperatures[choice-1],converted))
    

def is_number():
    temp = input('Δώσε θερμοκρασία σε βαθμούς Κελσίου: ')
    temp2 = temp.replace('-','',1)
    temp3 = temp2.replace('.','',1)
    if temp3.isdigit():  
        if float(temp) < -273.15:
            return 'λάθος'
        else:
             return temp    
    else: 
        return 'λάθος' 
       
main()


