#In this simple assignment you are given a number and have to make it negative. 
#But maybe the number is already negative?

def make_negative( number ):
    if number < 0:
        return number
    elif number > 0:
        return (0 - number)
    else:
        return 0
    

def make_negative_2( number ):
    return -abs(number)
    
    
print (make_negative(5))