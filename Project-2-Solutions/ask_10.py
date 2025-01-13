def checking_doubles(filename1, filename2):  
  f1 = open(filename1,'r')
  names1 = [line.split(',')[0] for line in f1] 
  del names1[0] #names1[0] = Όνομα (από την επικεφαλίδα)
  #names1[words[0]] = ( str(words[1]),str(words[2]),str( words[3].rstrip('\n') ) ) 
  f2 = open(filename2,'r')
  names2 = [line.split(',')[0] for line in f2]  
  del names2[0] #επικεφαλίδα
  double_names = set(names1).intersection(set(names2))
  f1.seek(0)
  f2.seek(0)
  line1_1 = f1.readline()
  line2_1 = f2.readline()
  doubles = {} #το λεξικό που θα επιστραφεί
  for line in f1:
      words = line.split(',')
      name = words[0]
      if name in double_names: 
        doubles[name] = {}
        doubles[name]['Αρχείο 1'] = (words[1],words[2],words[3].rstrip('\n'))
  for line in f2:
      words = line.split(',')
      name = words[0]
      if name in double_names: 
        doubles[name]['Αρχείο 2'] = (words[1],words[2],words[3].rstrip('\n'))
  return doubles

#print(checking_doubles('/Users/giannistsagaropoulos/Desktop/ena.csv', '/Users/giannistsagaropoulos/Desktop/dyo.csv'))

