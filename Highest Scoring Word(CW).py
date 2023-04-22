#Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#For example, the score of abad is 8 (1 + 2 + 1 + 4).
#You need to return the highest scoring word as a string.
#If two words score the same, return the word that appears earliest in the original string.
#All letters will be lowercase and all inputs will be valid.

def counting_score(word):                           
    alphabet = '0abcdefghijklmnopqrstuvwxyz'        # 0 at the beginning of the line
    score = 0                                       # because a = 1 point and must have index 1
    for char in word:                   
        score += alphabet.find(char)                # for each char count points and sum
    return score

def high(x):
    words = x.split()                               # split string on words
    table_score = {}
    for word in words:
        table_score[word] = counting_score(word)    # for each word count score and write to our table
    return max(table_score,key=table_score.get)     # return key from max of all values in the table

print(high('man i need a taxi up to ubud'))
print(high('aa b'))