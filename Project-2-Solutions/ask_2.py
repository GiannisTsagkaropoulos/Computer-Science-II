def code(string):
    codes = {'a':'0', 'b':'10', 'c':'110', 'd':'111'}
    encoded = ''
    for i in range(len(string)):
        if string[i] in list('abcd'):
            encoded += codes[string[i]]
        else:
            encoded += string[i]
    print(encoded)  
             
def decode(string):
    if string.endswith('101') or string.endswith('1111') or string.endswith('01') or string.endswith('011'):
        print('Not valid string to be decoded.')
    else:    
        decoded = ''
        count_of_ones = 0
        for ch in string:
            if ch == '1':
                count_of_ones += 1
            if ch == '0' or count_of_ones ==3:
                decoded += f'{chr(97+count_of_ones)}'
                count_of_ones = 0
        print(decoded)        

#code('abbabbabacdbdbdabd')
#decode('1010011100100100')

