#Make a program that filters a list of strings and returns a list with only your friends name in it.
#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
#Otherwise, you can be sure he's not...

def friend(x):
    my_friends = []
    i = 0
    for friend in x:
        if len(friend) == 4:
            my_friends[i] = friend
            i += 1
    return my_friends

print (friend(["Ryan", "Kieran", "Mark",]))
print (friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))