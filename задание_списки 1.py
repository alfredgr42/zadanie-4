n = int(input("Ведите колличество чисел: "))
list = []
for i in range(n):
   a = int(input("Введите значение болше 1, и меньше 10000: " ))
   if a>=1 and a<=10000:
     list.append(a)
else:
   print('Введите другое значение')
   print(list)
   print(list[::-1])
