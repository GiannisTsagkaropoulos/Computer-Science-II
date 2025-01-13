from curses.ascii import isalpha
import random
import copy
class Game:
    def __init__(self):
        S = []
        f = open('text.txt','w')
        f.write('non-governmental')
        f.close()
        f = open('text.txt','r')
        L = f.readlines()
        f.close()
        for i in range(len(L)): 
            L[i] = L[i].split()
            for ch in L[i]:
                for punc in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', ' ', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\n', '\t']:
                    ch = ch.rstrip(punc)
                S.append(ch)
        self.__word = S[random.randint(0,len(S)-1)].lower()
        temp = list(self.__word)
        self.__spaces =  []
        for i in temp:
            if i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', ' ', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\n', '\t']:
                pass
            else:
                self.__spaces.append(temp.index(i))
                temp[temp.index(i)] = ''
        self.__fails = 0
        self.__letters = []
    def show_word(self):
        L = list(self.__word)
        for i in self.__spaces:
            L[i] = '_'
        for j in L:
            print(j,end = ' ')
    def next_round(self):
        ind = []
        while True:
            letter = input('Give a letter: ').lower()
            try:
                if letter in self.__letters:
                    raise ValueError
                elif not letter.isalpha():
                    raise ZeroDivisionError
                elif len(letter) != 1:
                    raise AttributeError
                else:
                    self.__letters.append(letter)
            except ValueError:
                print('You have already said the letter!!')
            except AttributeError:
                print('The accepted antry is one character!!!')
            except ZeroDivisionError:
                print('The accepted antry is a character not a number!!!')
            else:
                break
        word = list(self.__word)
        for i in word:
            if i == letter:
                ind.append(word.index(i))
                word[word.index(i)] = 0
            else:
                pass
        return ind
    def evaluate(self):
        x = self.next_round()
        for i in x:
            self.__spaces.remove(i)
        if x == []:
            self.__fails += 1
    def play(self):
        self.show_word()
        while self.__fails < 6:
            self.evaluate()
            self.show_word()
            print('\n%s/6 mistakes !!'%(self.__fails))
            if self.__spaces == []:
                print('You win!!!')
                break
        else:
            print('You lose!!!') 