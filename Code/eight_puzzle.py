import search
import random
from statistics import mean

class EightPuzzle(search.Problem):
    """Traditional sliding-tile puzzle. A state is represented as a tuple of characters, '_' and '1' through '8'.
    The first three characters are the top row, the next three the middle row, and the last three the bottom row.
    An action is represented as the index of the position where the blank is being moved."""
    def __init__(self, n):
        """The initial state is formed by making n random moves from the goal state. Note that the shortest distance to
        the goal may be less than n because some random moves 'cancel out' others."""
        self.initial = tuple('_12345678')
        for i in range(n):
            action = random.choice(self.actions(self.initial))
            self.initial = self.result(self.initial, action)

    def actions(self, state):
        """Returns the list of actions available from state."""
        index = state.index('_')

        actions = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4, 6),
                    4: (1, 3, 5, 7), 5: (2, 4, 8), 6: (3, 7), 7: (6, 4, 8),
                    8: (5, 7)}
        return actions[index]

    def goal_test(self, state):
        """Returns true if state corresponds to _12345678."""
        return state == tuple('_12345678')

    def result(self, state, action):
        """Returns the state resulting from taking action in state."""
        new = list(state)
        a = new.index('_')

        new[action], new[a] = new[a], new[action]

        return tuple(new)


def prettify(state):
    """Returns a more human-readable grid representing state."""
    result = ''
    for i, tile in enumerate(state):
        result += tile
        if i % 3 == 2:
            result += '\n'
    return result


def misplaced(node):
    """8-puzzle heuristic returning the number of mismatched tiles."""
    answer = ('_12345678')
    mismatched = 0

    for i in range(len(answer)):
        if node.state[i] != answer[i]:
            mismatched += 1

    return mismatched


def manhattan(node):
    """8-puzzle heuristic returning the sum of Manhattan distance between tiles and their correct locations.
        Tiles have been represented as coordinates to solve for the distance between current and correct locations"""
    coordinates = {0: (0, 0), 1: (1, 0), 2: (2, 0),
                        3: (0, 1), 4: (1, 1), 5: (2, 1),
                        6: (0, 2), 7: (1, 2), 8: (2, 2)}
    answer = tuple('_12345678')
    manhattan = 0

    for i, answer in enumerate(answer):
        current_coordinates = coordinates[node.state.index(answer)]
        final_coordinates = coordinates[i]
        if current_coordinates != final_coordinates:
            manhattan += (abs(current_coordinates[0] - final_coordinates[0]) +
                            abs(current_coordinates[1] - final_coordinates[1]))

    return manhattan


if __name__ == '__main__':
    depths = (1, 2, 4, 8, 16)
    trials = 100
    path_lengths = {}
    state_counts = {}
    for depth in depths:
        print('Gathering data for depth ' + str(depth) + '...')
        path_lengths[depth] = {'BFS':[], 'IDS':[], 'A*-mis':[], 'A*-Man':[]}
        state_counts[depth] = {'BFS':[], 'IDS':[], 'A*-mis':[], 'A*-Man':[]}
        for trial in range(trials):
            puzzle = EightPuzzle(depth)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['BFS'].append(len(search.breadth_first_search(p).path()))
            state_counts[depth]['BFS'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['IDS'].append(len(search.iterative_deepening_search(p).path()))
            state_counts[depth]['IDS'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['A*-mis'].append(len(search.astar_search(p, misplaced).path()))
            state_counts[depth]['A*-mis'].append(p.states)
            p = search.InstrumentedProblem(puzzle)
            path_lengths[depth]['A*-Man'].append(len(search.astar_search(p, manhattan).path()))
            state_counts[depth]['A*-Man'].append(p.states)
    print('Path lengths:')
    print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}'.format('Depth', 'BFS', 'IDS', 'A*-mis', 'A*-Man'))
    for depth in depths:
        print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}' \
              .format(depth,
                      mean(path_lengths[depth]['BFS']),
                      mean(path_lengths[depth]['IDS']),
                      mean(path_lengths[depth]['A*-mis']),
                      mean(path_lengths[depth]['A*-Man'])))
    print('Number of states generated (not counting initial state):')
    print('{:>5}  {:>8}  {:>8}  {:>8}  {:>8}'.format('Depth', 'BFS', 'IDS', 'A*-mis', 'A*-Man'))
    for depth in depths:
        print('{:>5}  {:>8.1f}  {:>8.1f}  {:>8.1f}  {:>8.1f}'\
              .format(depth,
                      mean(state_counts[depth]['BFS']),
                      mean(state_counts[depth]['IDS']),
                      mean(state_counts[depth]['A*-mis']),
                      mean(state_counts[depth]['A*-Man'])))
