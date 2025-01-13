def primes(n): 
    L=list(range(2,n+1))
    plist = [] #initialization of primes list
    while L != []:
        plist.append(L.pop(0))
        last_prime = plist[len(plist)-1]
        for i in range(2*last_prime,n+1,last_prime): #αφαιρώ τα πολλαπλάσια του last prime και ξεκινώ από το 1ο
            if i >= L[len(L)-1]:
                break
            else:
                try:
                    L.remove(i)
                except ValueError:
                    continue
                
    print(plist)

primes(10011)