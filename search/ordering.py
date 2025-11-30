from search.heuristic import evaluate
from game.engine import result, player

def order_moves(state,moves):
    pl=player(state)
    scored=[(evaluate(result(state,mv)),mv) for mv in moves]
    if pl=="X":
        scored.sort(key=lambda x:(-x[0],x[1]))
    else:
        scored.sort(key=lambda x:(x[0],x[1]))
    return [mv for _,mv in scored]
