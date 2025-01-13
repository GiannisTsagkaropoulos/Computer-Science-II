def  dec2bin(n): 
    AkeraioMeros = abs(n) #αν n<0 ίδια διαδικασία και τυπωώνω με '-' 
    aker = []  #holds digits of integer part of the number
    #Integer part
    if AkeraioMeros < 1:
        aker = [0]
    else:           
        while AkeraioMeros != 0:  
            aker.append(AkeraioMeros%2)
            AkeraioMeros = AkeraioMeros//2 
        aker = aker[::-1]  #reversed
    if n < 0:    	
        print('-', end='')
    for i in range(len(aker)):
            print(aker[i],end = '')       
   
def  bin2dec(n): 
    y = str(n)
    num = 0  #holds digits of integer part of the number
    for i in range(0,len(y)): 
        i_osto_digit = int(y[:len(y)-i])%10
        num += i_osto_digit * (2**i)   
    print(num)     

# dec2bin(-11490280)   
# bin2dec(101001001001001001010001001111110)