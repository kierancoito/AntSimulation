import variables as v
import numpy as np
def initPherGrid(grid_size):
    '''Generate pheromone list
    Precondition:
    - grid_size = size of the grid

    Postcondition:
    - grid = grid with pheromones set up
    '''
    grid = np.zeros((grid_size+2, grid_size+2))
    grid[:,0] = np.ones(grid_size+2)*0.1*-1
    grid[:,-1] = np.ones(grid_size+2)*0.1*-1
    grid[0,:] = np.ones(grid_size+2)*0.1*-1
    grid[-1,:] = np.ones(grid_size+2)*0.1*-1
    print(grid[1:-1,int(grid_size/2)+1])
    grid[int(grid_size/2)+1,1:-1] = 50*(np.arange(grid_size)+1)/10
    return grid

test = initPherGrid(5)