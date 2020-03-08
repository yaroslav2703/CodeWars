def order(sentence):
  myList = sentence.split(' ')
  set1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  dic = {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'', '9':''}
  for i in myList:
      for symbol in i:
          if symbol in set1:
              dic[symbol] = i
              break
  s = dic['1'] + ' ' + dic['2'] + ' ' + dic['3'] + ' ' + dic['4'] + ' ' + dic['5'] + ' ' + dic['6'] + ' ' + dic['7'] + ' ' + dic['8'] + ' ' + dic['9']
  return s.strip()


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
