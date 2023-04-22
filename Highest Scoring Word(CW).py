#Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#For example, the score of abad is 8 (1 + 2 + 1 + 4).
#You need to return the highest scoring word as a string.
#If two words score the same, return the word that appears earliest in the original string.
#All letters will be lowercase and all inputs will be valid.

def counting_score(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    score = 0
    for char in word:
        score += alphabet.find(char)
    return score

def high(x):
    words = x.split()
    table_score = {}
    for word in words:
        table_score[word] = counting_score(word)
    return max(table_score,key=table_score.get)

print(high('man i need a taxi up to ubud'))
print(high('aa b'))