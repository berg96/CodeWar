#Write a function that takes a string of braces, and determines if the order of the braces is valid. 
#It should return true if the string is valid, and false if it's invalid.

def valid_braces(string):
    check = ''
    if string[0] == ')' or string[0] == ']' or string[0] == '}':
        return False
    for brace in string:
        if brace == '(' or brace == '[' or brace == '{':
            check += brace
        else:
            if (check[len(check)-1] == '(' and brace == ')') or (check[len(check)-1] == '[' and brace == ']') or   (check[len(check)-1] == '{' and brace == '}'):
                check = check[:-1]
            else:
                return False
    if len(check) != 0:
        return False
    else:
        return True

print (valid_braces("{}()[]"))
print (valid_braces("([{}])"))
print (valid_braces(")(){}"))