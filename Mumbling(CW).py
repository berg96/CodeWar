#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    new_string = ''
    i = 0
    for char in s:
        new_string += char.upper() + char.lower()*i + '-'
        i += 1
    return new_string[:-1]

print (accum("abcd"))
print (accum("ZpglnRxqenU"))