#Implement a function that receives two IPv4 addresses, 
#and returns the number of addresses between them (including the first one, excluding the last one).
#All inputs will be valid IPv4 addresses in the form of strings. 
#The last address will always be greater than the first one.

def count_ips(list):
    count = 0
    for i in range (4):
        count += (int(list[i]))*(256**(3-i))
    return count


def ips_between(start, end):
    start_ip = start.split('.')
    end_ip = end.split('.')
    return count_ips(end_ip) - count_ips(start_ip)


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("20.0.0.10", "20.0.1.0"))