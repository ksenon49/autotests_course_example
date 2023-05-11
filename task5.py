 ������ ������ ������
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
# ������ ����������� � ���������: �� ����� ����� num_people ������,
# ������� � ������� ����� ��� ������� �� ����� ������� kill_num �� �����.
# �� ������ ��������� �������, ��� �������� ���������, �� ����: ��������� ������� ������.
#
# num_people=7, kill_num=3 => ������ 7 ������� � ����� � ������ ������ �� ���� �������
# [1,2,3,4,5,6,7] - ��������� ����
# [1,2,4,5,6,7] => 3 �����
# [1,2,4,5,7] => 6 �����
# [1,4,5,7] => 2 �����
# [1,4,5] => 7 �����
# [1,4] => 5 �����
# [4] => 1 �����, 4 ������� ��������� �.�. �������� - ��� ��� ����� survivor.

def josephus_task(num_people, kill_num):
    survivor = []
    for person in range(1, num_people + 1):
        survivor.append(person)
    while len(survivor) > 1:
        for elem in range(0, kill_num - 1):
            survivor.append(survivor[elem])
        del survivor[:kill_num]
    survivor = survivor[0]
    return survivor
   
# ���� ������ �� ���� ��������


data = [
    (7, 3), (11, 19), (1, 300), (14, 2), (100, 1), (1234, 56), (987, 11)
]

test_data = [
    4, 10, 1, 13, 100, 1130, 379
]


for i, d in enumerate(data):
    assert josephus_task(*d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')