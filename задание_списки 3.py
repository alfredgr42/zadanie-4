m = int(input("������������ �����, ������� ����� ��������� ������: "))
n = int(input("����������� ������� ������� �� ������ ����: "))
mass = []
for i in range(n) :
i = int(input("������� ����� ������: "))
if m > i:
mass.append(i)
else:
print("������ ������, ����� � ����� �������")
mass.sort()
left = 0
right = len(mass) - 1
boat = 0
while left <= right:
if mass[left] + mass[right] <= m:
left +=1
right -= 1
boat += 1
print(f'���������� ����� ������� �����������: {boat}')