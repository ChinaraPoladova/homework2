
from game.state import initial_state
from search.minimax import minimax, reset_counter, get_nodes
from search.alphabeta import minimax_ab, reset_counter as reset_ab, get_nodes as get_nodes_ab

def test_minimax_vs_ab_initial():
    s = initial_state(3,3)
    reset_counter(); mv1 = minimax(s)
    reset_ab(); mv2 = minimax_ab(s)
    assert mv1 == mv2

def test_node_counts_compare():
    s = initial_state(3,3)
    reset_counter(); minimax(s); n1 = get_nodes()
    reset_ab(); minimax_ab(s); n2 = get_nodes_ab()
    assert n2 <= n1  # AB should explore no more nodes than plain minimax
