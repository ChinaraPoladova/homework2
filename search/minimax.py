
from game.engine import actions,result,utility,player

# node counter
nodes_explored = 0
def reset_counter():
    global nodes_explored
    nodes_explored = 0
def get_nodes():
    return nodes_explored

def minimax(state):
    if player(state) == "X":
        return _max(state)[1]
    return _min(state)[1]

def _max(state):
    global nodes_explored
    nodes_explored += 1
    u = utility(state)
    if u is not None:
        return float(u), None
    best = float("-inf")
    move = None
    for a in actions(state):
        v, _ = _min(result(state, a))
        if v > best or (v == best and (move is None or a < move)):
            best, move = v, a
    return best, move

def _min(state):
    global nodes_explored
    nodes_explored += 1
    u = utility(state)
    if u is not None:
        return float(u), None
    best = float("inf")
    move = None
    for a in actions(state):
        v, _ = _max(result(state, a))
        if v < best or (v == best and (move is None or a < move)):
            best, move = v, a
    return best, move
