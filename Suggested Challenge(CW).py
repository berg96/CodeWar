#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    n = arr[0]
    for i in range(len(arr)):
        if n != arr[i] and arr[i] != arr[i-1] and (arr[i] != arr[i-2] or arr[i] != arr[i-3]):
                n = arr[i]
    return n

def find_uniq_2(arr):
    two_elem = set(arr)
    for n in two_elem:
        if arr.count(n) == 1:
            return n

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 1, 1, 1, 1, 1, 2 ]))
print(find_uniq([ 7, 7, 7, 7, 7, 7, 6, 7 ]))
print(find_uniq_2([ 7, 7, 7, 7, 7, 7, 6, 7 ]))