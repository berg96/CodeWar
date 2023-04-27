#Write an algorithm that takes an array and moves all of the zeros to the end, 
#preserving the order of the other elements.

def move_zeros(lst):
    new_list = []
    count = 0
    for each in lst:
        if each != 0:
            new_list.append(each)
        else:
            count += 1
    for i in range(count):
        new_list.append(0)
    return new_list

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))