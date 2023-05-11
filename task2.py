# �������� ������� flatten_and_sort, ������� ��������� �������� ������ (������ �������) array,
# � ���������� "�������" ������ �� ����� ������� � ������� ����������� result_list
# �������� (���� --> �����) :
#
# [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]] -->  [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_and_sort(array):
    esult_list = []
    for lst in array:
        if type(lst) is list:
          for elem in lst:
            result_list.append(elem)
        else:
            result_list.append(lst)
    return (sorted(result_list))

# ���� ������ �� ���� ��������


data = [
    [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]],
    [[], []],
    [[], [1]],
    [[1, 3, 5], [100], [2, 4, 6]]
]

test_data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1], [1, 2, 3, 4, 5, 6, 100]
]


for i, d in enumerate(data):
    assert flatten_and_sort(d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')