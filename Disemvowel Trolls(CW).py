#Trolls are attacking your comment section!
#A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
#Your task is to write a function that takes a string and return a new string with all vowels removed.
#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def disemvowel(string_):
    string_ = delete_vowels(string_)
    return string_

def delete_vowels(string):
    for i in range(len(string)):
        if string[i] in ['a','e','i','o','u','A','E','I','O','U']:
            parts_of_string = string.split(string[i])
            parts_of_string[1] = delete_vowels(parts_of_string[1])
    return ''.join(parts_of_string)

print (disemvowel('This website is for losers LOL!'))