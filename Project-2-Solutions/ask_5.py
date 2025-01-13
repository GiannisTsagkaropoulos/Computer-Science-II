def encode(file_name, code):
    f = open(file_name,'r')
    lines = f.readlines()
    f.close()
    f = open(file_name,'w') #διαγράφεται παλιό κείμενο
    for line in lines:
        for ch_index in range(len(line)): #κάθε χαρακτήρας σε κάθε γραμμή
            ch = line[ch_index]
            if ch in code:
                f.write(code[ch])
            else:
                f.write(ch) 
    f.close()         

def decode(file_name, code):
    #creating decode_dict
    decode_d = {}
    for key in code:
        decode_value = code[key]
        decode_d[decode_value] = key
    #    
    f = open(file_name,'r')
    lines = f.readlines()
    f.close()          
    f = open(file_name,'w') #διαγράφεται παλιό κείμενο
    for line in lines:
        for ch_index in range(len(line)): #κάθε χαρακτήρας σε κάθε γραμμή
            ch = line[ch_index] 
            if ch in decode_d:
                f.write(decode_d[ch])
            else:
                f.write(ch) 
    f.close()         

