n = int(input("������ ����������� �����: "))
list = []
for i in range(n):
a = int(input("������� �������� ����� 1, � ������ 10000: " ))
if a>=1 and a<=10000:
list.append(a)
else:
print('������� ������ ��������')
print(list)
print(list[::-1])
