#Write a function that will return the count of distinct 
#case-insensitive alphabetic characters and numeric digits 
#that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    letters_numbers = {
        'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,
        'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,
        '0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0
    }
    for char in text.upper():
        letters_numbers[char] += 1
    count = 0
    for char in letters_numbers:
        if letters_numbers[char] >= 2:
            count +=1
    return count

def duplicate_count_2(text):
    seen = set()
    duples = set()
    for char in text:
        char = char.lower()
        if char in seen:
            duples.add(char)
        seen.add(char)
    return len(duples)

print (duplicate_count('abcde'))
print (duplicate_count('aabbcde'))