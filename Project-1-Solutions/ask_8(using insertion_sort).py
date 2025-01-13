List = []
def sumd(x):
    sumx = 0
    for i in str(x):
        sumx += int(i)
    return sumx

i = 100
while 999 >= i >= 100:
    List.append(i)
    i += 1

###insertion sort
for i in range(1, len(List)):
        temp = List[i]
        j = i-1
        while j >=0 and sumd(temp) >= sumd(List[j]) :
                List[j+1] = List[j]
                j -= 1
        List[j+1] = temp
###        
List.reverse()
print(List)