def generate_hashtag(s):
    words = s.split()
    if s == '':
        return False
    new_string = '#'
    for word in words:
        word.lower()
        new_string += word.title()
    if len(new_string) > 140:
        return False
    else:
        return new_string
    
def generate_hashtag_2(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output

print(generate_hashtag('      Codewars'))
print(generate_hashtag('CoDeWaRs is niCe'))
print(generate_hashtag_2('CoDeWaRs is niCe'))