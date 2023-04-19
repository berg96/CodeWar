#In this kata you are required to, given a string, 
#replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        if char.lower in alphabet:
            output += str(alphabet.find(char.lower)) + ' '
    return output[:-1]

print (alphabet_position("The sunset sets at twelve o' clock."))