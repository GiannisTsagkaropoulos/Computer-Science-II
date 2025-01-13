List = [ [] for digit_sum in range(27) ] #1ο στοιχείο λίστας όλοι οι 3ψήφιοι αριθμοί με άθροισμα 1

def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum    

for num in range(100,1000):
    digit_sum = sum_of_digits(num) #sum =5 έχει index = 4 στη λίστα
    List[digit_sum-1].append(num)

for i in range(len(List)):
    for j in List[i]:  
        print(j, end =', ')     
