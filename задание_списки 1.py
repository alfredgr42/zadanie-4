n = int(input("Âåäèòå êîëëè÷åñòâî ÷èñåë: "))
list = []
for i in range(n):
a = int(input("Ââåäèòå çíà÷åíèå áîëøå 1, è ìåíüøå 10000: " ))
if a>=1 and a<=10000:
list.append(a)
else:
print('Ââåäèòå äğóãîå çíà÷åíèå')
print(list)
print(list[::-1])
