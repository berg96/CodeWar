#Your goal in this kata is to implement a difference function, 
#which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    c = []
    for each in a:
        if each not in b:
            c.append(each)
    return c

print(array_diff([1,2], [1]))