def second(tup):
        return tup[1]

def most_occured_words(filename):
    f = open(filename, 'r')
    d = {}
    wordcounter = 0
    for line in f:
        words = line.split()
        wordcounter += len(words) #θέλω ποσοστό εμφάνισης αρά χρειάζομαι το σύνολο των λεέξων του κειμένου
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word]=1
    #d = {'word1':3, 'word2':4, 'word3':5, 'word4':2}                 
    l = list(d.items()) #[('word1':,3),('word2',4),('word3',5), ('word4',2)]
    l.sort(key = second) #[('word1',2),('word2',4),('word3',5), ('word4',2)]
    l = l[::-1] #sort τισ βάζει σε φθίνουσα εμφάνιση
    if len(l) >= 10:
        print('Οι 10 πιο συχνά εμφανιζόμενες λέξεις στο κείμενο είναι:\n')
        for i in range(10):
            pososto = format(100*l[i][1]/wordcounter, '.2f')
            print(l[i][0], 'με ποσοστό εμφάνισης :', pososto , '%', end = '\n')
    else:
        print('To κείμενο έχει',len(l), 'διαφορετικές λέξεις. Αυτές είναι:\n')
        for i in range(len(l)):
            pososto = format(100*l[i][1]/wordcounter, '.2f')
            print(l[i][0], 'με ποσοστό εμφάνισης :',pososto, '%', end = '\n')

most_occured_words('/Users/giannistsagaropoulos/Desktop/tes.txt')