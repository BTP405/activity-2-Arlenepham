
import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(t):
    text_file = open(t,'r')
    
        # read data from file, store them in integer 
    data = [int(line) for line in text_file.readlines()]

    text_file.close()
    
    x = ["0-10cms", "11-20cms", "21-30cms", "31-40cms", '41-50cms'] # ranges for the x-axis
    counts = [sum(1 for x in data if i < x <= i + 10) for i in range(0, 41, 10)] # counts the occurence for rach range

    # Plotting a vertical bar chart, style the bar color
    plt.bar(x, counts, color="#ffccff")
    
    # add text to the graph to display the value
    for index, value in enumerate(counts):
        plt.text(index, value, str(value))
    plt.yticks(np.arange(0, 4, step=1)) #values for y-axis
    
    #set labels and title
    plt.xlabel('Snowfall Ranges')
    plt.ylabel('Number of Days')
    plt.title('Snowfall  Distribution')

        
    # save the graph image 
    plt.savefig("q2.png")

    # show graph image
    plt.show()

graphSnowfall('./q2.txt')
