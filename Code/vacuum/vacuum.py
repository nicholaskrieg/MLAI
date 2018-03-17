"""
Visual aid to show difference between random walk, reflect, and state agents.
Simulates an automated Vacuum cleaner.

Python3
"""

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import random

WORLD_WIDTH = 25  # Width, in squares, of the world

# These are used by apply to update the agent's location
OFFSETS = {'north': (-1, 0),
           'south': (1, 0),
           'east': (0, 1),
           'west': (0, -1)}

# These are used by animate and draw_world to draw the world in color
EMPTY = 0.0
DIRT = 0.33
OBSTACLE = 0.67
AGENT = 1.0
cmap = matplotlib.colors.ListedColormap(['white', 'orange', 'black', 'blue'])
norm = matplotlib.colors.BoundaryNorm([0.0, 0.25, 0.5, 0.75, 1.0], cmap.N)


def random_world():
    """Creates and returns a random world."""
    # Create empty world
    grid = np.zeros((WORLD_WIDTH, WORLD_WIDTH))
    # Add dirt and obstacles
    for r in range(WORLD_WIDTH):
        for c in range(WORLD_WIDTH):
            if random.random() < 0.5:
                grid[r, c] = DIRT
            elif random.random() < 0.1:
                grid[r, c] = OBSTACLE
    # Place agent
    while True:
        r = random.randrange(WORLD_WIDTH)
        c = random.randrange(WORLD_WIDTH)
        if grid[r, c] == EMPTY:
            return grid, r, c


def get_percept(grid, r, c):
    """Returns the percept for an agent at position r, c on grid: 'dirty' or 'clean'."""
    if grid[r, c] == DIRT:
        return 'dirty'
    else:
        return 'clean'


def draw_world(grid, r, c, image):
    """Updates image, showing grid with the agent at r, c."""
    under = grid[r, c]
    grid[r, c] = AGENT
    image.set_data(grid)
    grid[r, c] = under


def apply(grid, r, c, action):
    """Applies action ('suck', 'north', etc.) for an agent at position r, c on grid."""
    if action == 'suck':
        grid[r, c] = EMPTY
    else:
        print(action)
        new_r = r + OFFSETS[action][0]
        new_c = c + OFFSETS[action][1]
        if 0 <= new_r < WORLD_WIDTH and 0 <= new_c < WORLD_WIDTH and grid[new_r, new_c] != OBSTACLE:
            return new_r, new_c
    return r, c


def animate(agent, steps, initialize=None):
    """Animates an agent's performance in a random world for the specified number of steps. initialize is called
    once to provide additional parameters to the agent."""
    grid, r, c = random_world()
    image = plt.imshow(grid, cmap=cmap, norm=norm)
    if initialize:
        state = initialize()
    for t in range(steps):
        draw_world(grid, r, c, image)
        percept = get_percept(grid, r, c)
        if initialize:
            action, *state = agent(percept, *state)
        else:
            action = agent(percept)

        r, c = apply(grid, r, c, action)
        plt.pause(0.0001)
    plt.show()


def score(grid):
    """Returns the number of non-dirty squares in grid."""
    result = 0
    for r in range(WORLD_WIDTH):
        for c in range(WORLD_WIDTH):
            if grid[r, c] != DIRT:
                result += 1
    return result


def simulate(agent, steps, initialize=None):
    """Simulates an agent's performance in a random world for the specified number of steps. Returns the total score
    over this time. initialize is called once to provide additional parameters to the agent."""
    grid, r, c = random_world()
    if initialize:
        state = initialize()
    result = 0
    for t in range(steps):
        result += score(grid)
        percept = get_percept(grid, r, c)
        if initialize:
            action, *state = agent(percept, *state)
        else:
            action = agent(percept)
        r, c = apply(grid, r, c, action)
    return result


def experiment(agent, steps, runs, initialize=None):
    """Repeatedly simulates agent in runs random worlds for the specified number of steps each. Returns the average
    score across runs. initialize is called at the beginning of each run to provide additional parameters to the
    agent."""
    result = 0
    for r in range(runs):
        result += simulate(agent, steps, initialize)
    return result / runs


def reflex_agent(percept):
    # if the current grid location is dirty, then suck
    # else return a direction (in this case, I choose north
    if percept is 'dirty':
        return 'suck'
    return 'north'


def random_agent(percept):
    # returns a random direction, if current grid location is dirty then it will suck
    if percept is 'dirty':
        return 'suck'
    return random.choice(['north', 'south', 'east', 'west'])


def state_agent(percept, dx, dy, map):
    # if current grid location is dirty, suck and insert suck at beginning of map
    # choose random action to start the state agent
    # choose an action that is random and not the same action as the previous
    # always insert new action to beginning of map
    # if previous action is 'suck', then pick an action that is not the same as
    # the second most previous

    if percept == 'dirty':
        map.insert(0, 'suck')
        return 'suck', dx, dy, map

    action = random.choice(['north', 'south', 'east', 'west'])

    if not map:
        action = random.choice(['north', 'south', 'east', 'west'])

    elif map[0] is 'north':
        dy -= 1
        action = random.choice(['east', 'west', 'north'])

    elif map[0] is 'south':
        dy += 1
        action = random.choice(['east', 'west', 'south'])

    elif map[0] is 'east':
        dx += 1
        action = random.choice(['north', 'south', 'east'])

    elif map[0] is 'west':
        dx -= 1
        action = random.choice(['north', 'south', 'west'])

    elif map[0] is 'suck':
        if map[1] is 'north':
            dy -= 1
            action = random.choice(['east', 'west', 'north'])

        elif map[1] is 'south':
            dy += 1
            action = random.choice(['east', 'west', 'south'])

        elif map[1] is 'east':
            dx += 1
            action = random.choice(['north', 'south', 'east'])

        elif map[1] is 'west':
            dx -= 1
            action = random.choice(['north', 'south', 'west'])

    map.insert(0, action)

    return action, dx, dy, map


def init_state_agent():
    # initalize the map and delta x and y variables here
    dx = 0
    dy = 0
    map = []

    return dx, dy, map



# Uncomment one of these to animate one of your agents
# animate(reflex_agent, 1000)
# animate(random_agent, 1000)
animate(state_agent, 1000, init_state_agent)

# Uncomment these to run experiments comparing performance of different agents
# NOTE: This will take a while!
# print('Reflex agent: ', experiment(reflex_agent, 10000, 20))
# print('Random agent: ', experiment(random_agent, 10000, 20))
print('State agent: ', experiment(state_agent, 10000, 20, init_state_agent))
