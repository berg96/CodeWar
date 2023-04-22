#You are given an array (which will have a length of at least 3, 
# but could be very large) containing integers. 
#The array is either entirely comprised of odd integers or entirely comprised of even integers
# except for a single integer N. 
#Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    if integers[0] % 2 == 0:            # if 1st elem is even
        if integers[1] % 2 == 0:        # if 2nd elem is even
            for i in integers:          # find odd elem
                if i % 2 != 0:
                    return i
        else:                           # 1st elem is even, 2nd is odd
            if integers[2] % 2 == 0:    # 3rd elem is even
                return integers[1]      # return 2nd elem
            else:                       # 3rd elem is odd
                return integers[0]      # return 1st elem
    else:
        if integers[1] % 2 != 0:        # 1st elem is odd, 2nd is odd
            for i in integers:          # find even elem
                if i % 2 == 0:
                    return i
        else:
            if integers[2] % 2 == 0:    # 1st is odd, 2nd is even, 3rd is even
                return integers[0]      # return 1st
            else:                       # 1st id odd, 2nd is even, 3rd is odd
                return integers[1]      # return 2nd
    return None

def find_outlier_2(integers):
    listEven = []
    listOdd = []
    for i in integers:
        if i % 2 == 0:
            listEven.append(i)
        else:
            listOdd.append(i)
    if len(listEven) == 1:
        return listEven[0]
    else:
    	return listOdd[0]

print (find_outlier([5219247, -3082459, 8656945, -8793873, -4071953, 6525061, 1510671, -8592321, 3359607, 4195759, -503223, 1888563, 863083, -3236743, -2985261, 3745871, 154581, -1908113, 4321625, -9817633, 479115, 4222071, 6023495, 9925647, 5582505, -1725403, 9809709, -2767534, -7195115, -5652955, -3063767, 527495, -5504461, -7658717]))