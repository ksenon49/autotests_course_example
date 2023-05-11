# �������� �������, ������� ��������� ������ num_tuple �� 10 ���� num_tuple,
# � ���������� ������ ���� ����� � ���� ������ �������� str_phone.
# �������� (���� --> �����) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    str_phone = '({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}'.format(*num_tuple)
    return str_phone

# ���� ������ �� ���� ��������


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')