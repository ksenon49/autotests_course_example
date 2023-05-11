# �������� ������� sum_digits, ������� ��������� ������������� ����� num,
# � ���������� ����� ���� our_sum.
# �������� (���� --> �����) :
#
# 39 --> 12
# 999 --> 27
# 4 --> 4

def sum_digits(num):
    our_sum = int()
    while num > 0:
        digit = num % 10
        our_sum += digit
        num //= 10
    return our_sum

# ���� ������ �� ���� ��������


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'� ������� {d} ���� ������, �� �������� ��������'
    print(f'�������� ����� {d} ������ ��������')
print('�� ��')