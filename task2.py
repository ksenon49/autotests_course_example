# ��� ������ �� 7 ��������� ���������. ��������� ������� (�� ������������ ����), ���������� �����:
# ����������� � ������������ �������� ������;
# ����� � ������� �������������� � ����������� �� 2 ������ ����� �������;

from statistics import mean
def get_list_info(*lst):
    min_elem = min(*lst)
    max_elem = max(*lst)
    sum_elem = sum(*lst)
    average = round((sum(*lst)/len(*lst)), 2)
    return min_elem, max_elem, sum_elem, average

# ���� ������ �� ���� ��������


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    (1, 7, 28, 4.0), (-7, -1, -28, -4.0), (-308, 209, 68, 9.71), (-3, 3, 0, 0.0)
]


for i, d in enumerate(data):
    assert get_list_info(d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')
# 123