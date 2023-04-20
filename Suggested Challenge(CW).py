#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    n = arr[0]
    for i in range(len(arr)-1):
        if n != arr[i]:
            if n != arr [i+1]:
                return n
            else:
                return arr[i+1]
        else:
            return arr[i]
    return n 

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))