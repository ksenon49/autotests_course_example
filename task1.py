# ���������� ��������.
# ������� ��������� ����������, ������������ � ���������� ������� ��������� ������:
# number = 1
# string = 'Hello'
# �������� � �������� �������, ������� ����� �������� � ���������� ��� ����������, �� ��������� ��������:
# number = 5
# string = 'Hello, dear friend'
# 

number = 1
string = 'Hello'


def global_changes():
    global number, string
    number = 5
    string = 'Hello, dear friend'
    return number, string


global_changes()



# ���� ������ �� ���� ��������
assert number == 5, '���������� number ������ ����� �������� 5'
assert string == 'Hello, dear friend', '���������� string ������ ����� �������� Hello, dear friend'
assert global_changes() == (5, 'Hello, dear friend')

print('��� ��')
