#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    n = arr[0]
    for i in range(len(arr)):
        if n != arr[i] and arr[i] != arr[i-1] and (arr[i] != arr[i-2] or arr[i] != arr[i+1]):
                n = arr[i]
    return n

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 1, 1, 1, 1, 1, 2 ]))