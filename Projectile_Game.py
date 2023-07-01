%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import random
import numpy as np

# Generate random wall coordinates
random_wall_x = [random.uniform(-10, 10) for _ in range(3)]
random_wall_y = [random.uniform(-10, 10) for _ in range(3)]


def parabola_game(a, b, c):
    # x and y values
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    points = 10*(xmax - xmin)
    x = np.linspace(xmin, xmax, points)

    # Parabola equation
    y = a*x**2 + b*x + c

    # Plotting
    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'black')
    plt.plot([0, 0], [ymin, ymax], 'black')

    # Plot the wall
    for i in range(3):
        plt.plot([random_wall_x[i], random_wall_x[i]], [0, random_wall_y[i]], 'red')


    plt.plot(x, y, 'c')
    plt.grid()
    plt.show()

print("Easy: Press 1\nDifficult: Press 2\n")
user_choice = int(input("Enter your preference: "))

if user_choice == 1:
    interactive_plot = interactive(parabola_game, a=(-10, 10), b=(-10, 10), c=(-10, 10))
    interactive_plot
elif user_choice == 2:
    stop_or_go = 1
    while stop_or_go:
        a = int(input("Enter your a value: "))
        b = int(input("Enter your b value: "))
        c = int(input("Enter your c value: "))
        parabola_game(a, b, c)
        stop_or_go = int(input("If you want to keep going, press 1. To stop, press 0. "))
else:
    print("Invalid choice.")
