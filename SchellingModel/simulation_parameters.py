import numpy as np
import movement_tactics as tactics


side = 50   # size of grid
empty_fraction = 0.3    # fraction of empty cells
types_distribution = [0.33, 0.33, 0.34]  # distribution of each type, among non-empty cells
type_colours = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]   # colour of each type of cell
# adjacency matrix. Denotes how well (or not well) two types get along
# Values between -1 and 1
# 0 doesn't affect the neighbourhood_value
# Ideally, keep the diagonal 1 (everyone gets along with the same type)
gets_along_with = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])
type_matrix = np.zeros((side, side), dtype=int)  # type of (i, j) node
empty_colour = (0.3, 0.3, 0.3)    # colour of empty cells
max_iterations = 500  # maximum iterations the simulation will run for
neighbour_amount = 0.75  # what threshold of neighbourhood_score is stable?
# what movement tactic is used. For implementation reasons, this must be a type and not an object
tactic = tactics.TargetedMovement
types = len(types_distribution)

grid_history = []
empty_nodes = set()
