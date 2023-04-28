#Write a function that takes an integer as input, 
#and returns the number of bits that are equal to one in the binary representation of that number. 
#You can guarantee that input is non-negative.

def count_bits(n):
    count = 0
    while n > 0:
        if n % 2 != 0:
            count += 1
        n = int(n/2)
    return count

print(count_bits(4))
print(count_bits(10))
print(count_bits(0))