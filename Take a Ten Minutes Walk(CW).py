#You live in the city of Cartesia where all roads are laid out in a perfect grid. 
#You arrived ten minutes too early to an appointment, 
#so you decided to take the opportunity to go for a short walk. 
#The city provides its citizens with a Walk Generating App on their phones -- 
#everytime you press the button 
#it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
#You always walk only a single block for each letter (direction) 
#and you know it takes you one minute to traverse one city block, 
#so create a function that will return true 
#if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
#and will, of course, return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    if len(walk) == 10:
        coordinates = [0,0]
        for step in walk:
            if step == 'n':
                coordinates[0] += 1
            elif step == 's':
                coordinates[0] -= 1
            elif step == 'w':
                coordinates[1] -= 1
            elif step == 'e':
                coordinates[1] += 1
        if coordinates[0] == 0 and coordinates[1] == 0:
            return True
        else:
            return False
    else:
        return False
    
print (is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print (is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print (is_valid_walk(['s', 'w', 'e', 's', 'n', 'e', 'w', 'n']))