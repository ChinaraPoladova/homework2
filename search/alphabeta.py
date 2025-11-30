
from game.engine import actions,result,utility,player
from search.ordering import order_moves

nodes_explored = 0
def reset_counter():
    global nodes_explored
    nodes_explored = 0
def get_nodes():
    return nodes_explored

def minimax_ab(state):
    if player(state) == "X":
        return maxab(state, -1e9, 1e9)[1]
    return minab(state, -1e9, 1e9)[1]

def maxab(state, alpha, beta):
    global nodes_explored
    nodes_explored += 1
    u = utility(state)
    if u is not None:
        return float(u), None
    best = -1e9
    move = None
    for a in order_moves(state, actions(state)):
        v, _ = minab(result(state, a), alpha, beta)
        if v > best or (v == best and (move is None or a < move)):
            best, move = v, a
        alpha = max(alpha, best)
        if alpha >= beta:
            break
    return best, move

def minab(state, alpha, beta):
    global nodes_explored
    nodes_explored += 1
    u = utility(state)
    if u is not None:
        return float(u), None
    best = 1e9
    move = None
    for a in order_moves(state, actions(state)):
        v, _ = maxab(result(state, a), alpha, beta)
        if v < best or (v == best and (move is None or a < move)):
            best, move = v, a
        beta = min(beta, best)
        if alpha >= beta:
            break
    return best, move
