# Assignment 1
# CSC 486 - Spring 2022
# Author: Dr. Patrick Shepherd

# Purpose: to test your installation of PyCharm and make sure some of our common
# libraries are installed and working correctly.

import networkx
import matplotlib.pyplot as plt

def main():

    # Draws a complete graph of 10 nodes, then presents it on the screen.
    # Visit https://networkx.org/documentation/stable/reference/generators.html for
    # a lot of alternatives to complete_graph() that you can play around with!
    G = networkx.complete_graph(10)
    networkx.draw(G)
    plt.show()

if __name__ == '__main__':
    main()
