#Implement a function that receives two IPv4 addresses, 
#and returns the number of addresses between them (including the first one, excluding the last one).
#All inputs will be valid IPv4 addresses in the form of strings. 
#The last address will always be greater than the first one.

def ips_between(start, end):
    start_ip = start.split('.')
    end_ip = end.split('.')
    between = 0
    for each in start_ip:
        int(each)
    for each in end_ip:
        int(each)
    if start_ip[3] > end_ip[3]:
        if end_ip[2] !=0:
            end_ip[2] -= 1
        else:
            if end_ip[1] != 0:
                end_ip[1] -= 1
                end_ip[2] += 254
            else:
                end_ip[0] -= 1
                end_ip[1] += 254
        end_ip[3] += 255
    if start_ip[2] > end_ip[2]:
        if end_ip[1] !=0:
            end_ip[1] -= 1
        else:
            end_ip[0] -= 1
            end_ip[1] += 254
        end_ip[2] += 255
    if start_ip[1] > end_ip[1]:
        end_ip[0] -= 1
        end_ip[1] += 255
    return (end_ip[3]-start_ip[3]+255*(end_ip[2]-start_ip[2])+255*255*(end_ip[1]-start_ip[1])+255*255*255*(end_ip[0]-start_ip[0]))

print(ips_between("10.0.0.0", "10.0.0.50"))