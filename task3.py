# ��� ������. ������� ����� ��������� � ������� ���������


def even_sum(lst1):
    sum_list = sum(lst1[::2])
    return sum_list

# ���� ������ �� ���� ��������


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    16, -16, 338, 0
]


for i, d in enumerate(data):
    assert even_sum(d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')