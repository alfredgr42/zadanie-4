n = int(input("������ ����������� ����� >=1 � <=1000000 "))
list = []
for i in range(n):
a = int(input("������� �������� ����� 1, � ������ 10000: " ))
if a >=1 and a <=100000:
list.append(a)
else:
print("������� ������ �����")
a = list.pop(-1)
list.insert(0, a)
print(list)