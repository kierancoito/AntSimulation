import numpy as np
import variables

antProbability = 0.6

def initAntGrid(n):
    grid = np.array((n + 2, n + 2))
    grid[0:] = variables.BORDER
    grid[-1:] = variables.BORDER
    grid[:0] = variables.BORDER
    grid[:-1] = variables.BORDER

    for i in range(1, n-1):
        for j in range(1, n-1):
            if np.random.random() < antProbability:
                randomDirection = np.random.randint(0,4)

                grid[i][j] =

    return