from game.engine import terminal, utility
from game.lines import lines

def evaluate(state):
    if terminal(state):
        return 1000*utility(state)
    score=0
    grid=state["grid"]; m=state["m"]; k=state["k"]
    for L in lines(m,k):
        vals=[grid[r][c] for (r,c) in L]
        x=vals.count("X"); o=vals.count("O")
        if x>0 and o>0: continue
        if x>0: score+=10**(x-1)
        if o>0: score-=10**(o-1)
    return score
