def wordCount(t):
    file = open(t,'r')
    
    # strip() : to remove the newline
    #lower() : to make all words lowercase
    #split() : convert a string into a list of smaller strings separated by " "
    lines = [line.strip().lower().split(" ")  for line in file]
    file.close()
    
    print(lines)
    
    d = dict() # create an empty dictionary
    i = 1

    for line in lines:
        for fruit in line: 
            if fruit in d:  #if fruit exists
                d[fruit].append(i) # append the line where fruit appears into the value list of fruit
            else: 
                d[fruit] = [i] # add the pair of fruit and a list containing what line it appears
        i += 1
    return d

check = wordCount('q3.txt')

for key in list(check): 
    print(key, ":", check[key])   
