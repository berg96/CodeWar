def descending_order(num):
    list_of_num = []
    num_str = str(num)
    for each in num_str:
        list_of_num.append(each)
    list_of_num.sort(reverse=True)
    output = ''
    for each in list_of_num:
        output += each
    return int(output)


def Descending_Order_2(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)


print(descending_order(51))