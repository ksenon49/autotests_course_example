# ����������� ���������
# ������� ������� global_function � ��������� ���������� msg = 1
# ���� ������ ��������� ������ ������� global_function ��������� �������:
# global_function ������ ��������� � ���� ������� local_function
# local_function ������ �������� �������� ���������� msg �� �������� 2


def global_function():
    msg = 1

    def local_function():
        nonlocal msg
        msg += 1

    local_function()
    return msg

	
assert global_function() == 2, '�������� ���������� msg ������ ���� ����� 2'
print('��� ��')