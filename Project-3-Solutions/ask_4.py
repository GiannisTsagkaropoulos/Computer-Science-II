import time
class Item:
    def __init__(self,name,priority):
        self.name = name
        self.priority = priority
        self.time = time.time()
class Priority_queue:
    def __init__(self,List = []):
        flag = True
        for i in List:
            if type(i) != Item:
                flag = False
                break
        if flag:        
            self.__que = List
        else:
            self.__que = list()
            print('Η λίστα προτεραιότητας μπορεί να περιέχει μόνο αντικείμενα τύπου Item. Αντικατέστησα τη λίστα που εισήχθη με την κενή λίστα.')    
        
    def insert(self): 
        name = input('Give Name: ')
        while True:
            priority = input('Give the number of priority: ')
            try:
                priority = int(priority)
            except ValueError:
                print('The accepted value is a number!!')
                continue
            else:
                break
        self.__que.append(Item(name,priority))
    def eject(self):
        M = self.__que[0]
        for i in self.__que:
            if i.priority < M.priority: 
                M = i 
            elif i.priority == M.priority and i.time < M.time:
                M = i
            else:
                continue
        print('Επομενος: %s'%(M.name))
        self.__que =self.__que.remove(M)

a = Priority_queue()
a.insert()
a.insert()