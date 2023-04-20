#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    num = arr[0]
    for i in range(len(arr)):
        if num != arr[i]:
            if num != arr [i+1]:
                n = num
            else:
                n = arr[i+1]
        else:
            n = arr[i]
    return n 

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))