
def decorator(func):
    def inner(numbers):
        # Call the original function to retrieve numbers
        lines = func(numbers)

        for line in lines: 
            print("Numbers:", line)
            print("Count:", len(line))
            print("Average:", sum(line) / len(line))
            print("Maximum:", max(line))
    return inner

  

#@decorator -- another way to apply decorator to function
def printStats(t):
    file = open(t,'r')
    lines = file.readlines()
    # split() splits the line into an array. 
    # map() apply int() to each splited element. 
    # list() converts the iterator returned by map() into a list. 
    return [list(map(int, line.split())) for line in lines]

decorated_function = decorator(printStats)
decorated_function('q4.txt')





