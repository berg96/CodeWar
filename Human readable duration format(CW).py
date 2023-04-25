#The function must accept a non-negative integer. If it is zero, it just returns "now". 
#Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    result = []
    if (seconds % 60) > 1:
        result.append(str(seconds % 60) + ' seconds')                            #result[0]
    elif (seconds % 60) == 1:
        result.append(str(seconds % 60) + ' second')
    elif (seconds % 60) == 0:
        result.append(0)
    if (int(seconds / 60) % 60) > 1:
        result.append(str(int(seconds / 60) % 60) + ' minutes')                            #result[0]
    elif (int(seconds / 60) % 60) == 1:
        result.append(str(int(seconds / 60) % 60) + ' minute')
    elif (int(seconds / 60) % 60) == 0:
        result.append(0)
    if (int((seconds / 60) / 60) % 24) > 1:
        result.append(str(int((seconds / 60) / 60) % 24) + ' hours')                            #result[0]
    elif (int((seconds / 60) / 60) % 24) == 1:
        result.append(str(int((seconds / 60) / 60) % 24) + ' hour')
    elif (int((seconds / 60) / 60) % 24) == 0:
        result.append(0)
    if (int(((seconds / 60) / 60) / 24) % 365) > 1:
        result.append(str(int(((seconds / 60) / 60) / 24) % 365) + ' days')  
    elif (int(((seconds / 60) / 60) / 24) % 365) == 1:
        result.append(str(int(((seconds / 60) / 60) / 24) % 365) + ' day')
    elif (int(((seconds / 60) / 60) / 24) % 365) == 0:
        result.append(0)
    if (int((((seconds / 60) / 60) / 24) / 365)) > 1:
        result.append(str(int((((seconds / 60) / 60) / 24) / 365)) + ' years')  
    elif (int((((seconds / 60) / 60) / 24) / 365)) == 1:
        result.append(str(int((((seconds / 60) / 60) / 24) / 365)) + ' year')
    elif (int((((seconds / 60) / 60) / 24) / 365)) == 0:
        result.append(0)
    i = 0
    output = ''
    for each in result:
        if each != 0:
            if i == 0:
                output += each
                i += 1
            elif i == 1:
                output = each + ' and ' + output
                i += 1
            elif i > 1:
                output = each + ', ' + output
    return output

print(format_duration(1))
