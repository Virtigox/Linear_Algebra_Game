import matplotlib.pyplot as plt
import random

def scatter_plot_game(graph_size):
    # Set the range of x and y coordinates
    xmin, xmax = -graph_size, graph_size
    ymin, ymax = -graph_size, graph_size

    # Generate random coordinates
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'black')
    plt.plot([0, 0], [ymin, ymax], 'black')



    plt.xticks(range(xmin, xmax,2))  # Set the x-axis ticks linerly
    plt.yticks(range(ymin,ymax,2))

   # Plot the random coordinate
    ax.plot(x, y, 'ro')

    plt.tight_layout()
    plt.grid()
    plt.show()

    # Prompt player for input
    x_user = int(input("Enter the X value: "))
    y_user = int(input("Enter the Y value: "))

    # Check if the player's input matches the generated coordinates
    if x_user == x and y_user == y:
        print("You are right!")
    else:
        print(f"You are wrong. The correct coordinates are ({x}, {y})")

scatter_plot_game(50)  # Adjust the graph size as needed
