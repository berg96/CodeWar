def generate_hashtag(s):
    words = s.split()
    new_string = '#'
    for word in words:
        word.lower()
        new_string += word.title()
    return new_string

print(generate_hashtag('      Codewars'))
print(generate_hashtag('CoDeWaRs is niCe'))