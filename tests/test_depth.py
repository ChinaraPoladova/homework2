
from game.state import initial_state
from search.depth_limited import search_dl, reset_counter, get_nodes

def test_depth_block_immediate_win():
    s = initial_state(4,3)
    s["grid"][0][0] = "X"
    s["grid"][0][1] = "X"
    s["to_move"] = "X"
    reset_counter()
    mv = search_dl(s, depth=2)
    assert mv == (0,2)
