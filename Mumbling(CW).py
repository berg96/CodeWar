#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    new_string = ''
    i = 0
    for char in s:
        new_string += char.upper()
        if i > 0 :
            for j in range (i-1):
                new_string += char.lower()
        i += 1
        new_string += '-'
    return new_string.replace(new_string[len(new_string)-2],'')

print (accum("abcd"))