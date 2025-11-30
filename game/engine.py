from game.lines import lines
from game.state import copy_state

def player(state): return state["to_move"]

def actions(state):
    m=state["m"]
    out=[]
    for r in range(m):
        for c in range(m):
            if state["grid"][r][c] is None:
                out.append((r,c))
    return sorted(out)

def result(state,action):
    r,c=action
    s2=copy_state(state)
    s2["grid"][r][c]=state["to_move"]
    s2["to_move"]="O" if state["to_move"]=="X" else "X"
    return s2

def winner(state):
    grid=state["grid"]; m=state["m"]; k=state["k"]
    for L in lines(m,k):
        vals=[grid[r][c] for (r,c) in L]
        if all(v=="X" for v in vals): return "X"
        if all(v=="O" for v in vals): return "O"
    return None

def terminal(state):
    if winner(state): return True
    return not any(cell is None for row in state["grid"] for cell in row)

def utility(state):
    w=winner(state)
    if w=="X": return 1
    if w=="O": return -1
    if terminal(state): return 0
    return None
