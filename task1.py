def change(roll=[str]):
    roll = roll if roll else {}
    roll[0], roll[-1] = roll[-1], roll[0]
    print(roll)

uju = ['2', '4', '8']
change(uju)

# 2  минимальный и максимальный элементы списка
def get_list_info(lst):
    min_elem = {min(lst)}
    max_elem = {max(lst)}
    sum_elem = {sum(lst)}
    return min_elem, max_elem

get_list_info([1, 5, -7, 8, 4, 3,-8])
