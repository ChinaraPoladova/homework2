
import time, json
from game.state import initial_state
from search.minimax import minimax, reset_counter, get_nodes
from search.alphabeta import minimax_ab, reset_counter as reset_ab, get_nodes as get_nodes_ab
from search.depth_limited import search_dl, reset_counter as reset_dl, get_nodes as get_nodes_dl

def run_minimax(m,k):
    s = initial_state(m,k)
    reset_counter()
    t0 = time.time()
    mv = minimax(s)
    t1 = time.time()
    return {"move": mv, "time": t1-t0, "nodes": get_nodes()}

def run_ab(m,k):
    s = initial_state(m,k)
    reset_ab()
    t0 = time.time()
    mv = minimax_ab(s)
    t1 = time.time()
    return {"move": mv, "time": t1-t0, "nodes": get_nodes_ab()}

def run_dl(m,k,depth):
    s = initial_state(m,k)
    reset_dl()
    t0 = time.time()
    mv = search_dl(s, depth)
    t1 = time.time()
    return {"move": mv, "time": t1-t0, "nodes": get_nodes_dl()}

results = {}
# 3x3 comparison
results["3x3_minimax"] = run_minimax(3,3)
results["3x3_ab"] = run_ab(3,3)
# 4x4 depth-limited
results["4x4_dl_d2"] = run_dl(4,3,2)
results["4x4_dl_d4"] = run_dl(4,3,4)
# 5x5 depth-limited (k=4) shallow depth
results["5x5_dl_d3"] = run_dl(5,4,3)

print(json.dumps(results, indent=2))
# also save
with open("perf_results.json","w") as f:
    json.dump(results, f, indent=2)
