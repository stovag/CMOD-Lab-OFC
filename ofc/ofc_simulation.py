import random as r
import time
import numpy as np
from matplotlib import pyplot as plt

###########################################
# Application of the OFC model in python  #
# Evangelos Stogiannos                    #
###########################################

# neighboring_plates: function that receives the coordinates of the current grid
# cell and returns a list containing the coordinates of its neighbors


def neighboring_plates(i, j, n):
    plates = []
    if i-1 >= 0:
       plates.append([i-1, j])
    if i+1 < n:
        plates.append([i+1, j])
    if j-1 >= 0:
        plates.append([i, j-1])
    if j+1 < n:
        plates.append([i, j+1])
    return plates

# MAIN


def simulation(n, a, steps, force):
    limit = np.random.normal(0.5, 0.175, (n, n))  # Randomly generated limit for each grid cell
    grid = np.zeros((n, n))  # First iteration of the grid, filled with 0s
    current_step = 1  # current_step steps
    magnitude_list = []  # list of the broken cells in each current_step step
    total_force_list = []  # list of the total force of the grid in each current_step step

    # (ln 41~47) In each current_step step, add force to each cell in the grid
    # (ln 48~58) If a cell exceeds the limit and breaks, increase the magnitute by 1 and set it's force to 0.
    #            Set the flag to 1 and create x and y as the coordinates for the neighboring cells
    # (ln 59~71 )If at least a cell has been broken, repeat the above for each neighboring cell,
    #            changing the values of x and y to match the last broken cell's until no cell's meighnors
    #            have been broken. If no cells are broken the flag is set to 0 and the loop ends, moving
    #            on to the next current_step step

    t0 = time.time()
    while current_step < steps:
        curr_magnitude = 0  # number of broken cells
        grid += force
        for i in range(n):
            for j in range(n):
                if grid[i][j] > limit[i][j]:
                    curr_magnitude = curr_magnitude + 1
                    force_dissipated = grid[i][j] * a
                    grid[i][j] = 0
                    flag_broken = 1   # Flag for when a cell breaks. If the flag is 1 the force dissipation continues
                    x = i
                    y = j
                    while flag_broken == 1:
                        broken_neighbors = 0
                        for k in neighboring_plates(x, y, n):
                            grid[k[0]][k[1]] = grid[k[0]][k[1]] + force_dissipated
                            if grid[k[0]][k[1]] > limit[k[0]][k[1]]:
                                curr_magnitude = curr_magnitude + 1
                                force_dissipated = grid[k[0]][k[1]] * a
                                grid[k[0]][k[1]] = 0
                                broken_neighbors = broken_neighbors + 1
                                x = k[0]
                                y = k[1]
                        if broken_neighbors == 0:
                            flag_broken = 0

        total_force = sum(grid[t][s] for t in range(n) for s in range(n))  # sum of each cell's force
        current_step = current_step + 1
        magnitude_list.append(curr_magnitude)  # Add the number of broken cells in the list
        # total_force_list.append(total_force) # Add the total force to the list
        # print("Step:", current_step, "Broken:", magnitude)
        # print("Total force", total_force)

    # Plot the sorted magnitude list
    magnitude_list.sort()
    plt.plot(magnitude_list)
    display = plt.show()
    return display

# #Plot the grid's total force in each current_step step
# plt.plot(total_force_list)
# plt.show()
