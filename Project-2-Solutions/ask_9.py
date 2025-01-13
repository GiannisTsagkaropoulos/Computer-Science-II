def prosfora(filename):
    f = open(filename,'r')
    line1 = f.readline() #επικεφαλίδα
    sale_value = 0
    fpa = 0
    summed = 0
    for line in f:
        words = line.split(',') 
        sale_value += float(words[1])*float(words[2])
        fpa += float(words[1])*float(words[2])*float(words[3].rstrip('%\n'))
    summed = sale_value + fpa    
    f.close()
    print('Η συνολική καθαρή αξία της προσφοράς χωρίς ΦΠΑ είναι',sale_value,'Το συνολικό ποσό \
         του ΦΠΑ είναι: ',fpa,'και την συνολική αξία της προσφοράς μαζί με ΦΠΑ είναι :',summed)    
    
