def insertion_sort(List):
    for i in range(1,len(List)):
        temp = List[i]
        j = i - 1 
        while j >= 0 and temp <= List[j]:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = temp
    return List

print(insertion_sort([223,23,23,54,4,5,34,4,56,345,67,4,56,567,-3]))