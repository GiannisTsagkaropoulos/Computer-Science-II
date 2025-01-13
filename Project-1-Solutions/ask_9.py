def lex(word):
    if '0' not in word:
       return ('0'*(len(word)+1))
    else:    
        for i in range(len(word)):
            str1 = ''
            l=list(word)
            if word[len(word)-1-i]=='0':
                l[len(word)-1-i] = '1'
                for j in range(1,i+1):
                    l[len(word)-1-i+j]='0'
                return (str1.join(l))
                break
    


