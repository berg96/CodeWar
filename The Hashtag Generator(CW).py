def generate_hashtag(s):
    words = s.split()
    new_string = '#'
    for word in words:
        new_string += word
    return new_string

print(generate_hashtag('      Codewars'))