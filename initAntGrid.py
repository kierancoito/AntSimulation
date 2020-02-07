import numpy as np
import variables

antProbability = 0.6

def initAntGrid(n):
    grid = np.zeros((n+2, n+2))
    grid[:,0] = np.ones(n+2) * variables.BORDER
    grid[:,-1] = np.ones(n+2) * variables.BORDER
    grid[0,:] = np.ones(n+2) * variables.BORDER
    grid[-1,:] = np.ones(n+2) * variables.BORDER

    for i in range(1, n-1):
        for j in range(1, n-1):
            if np.random.random() < antProbability:
                randomDirection = np.random.randint(1,high=5)
                grid[i][j] = float(randomDirection)

    return grid
print(initAntGrid(6))