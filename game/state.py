from typing import List, Optional

BoardGrid = List[List[Optional[str]]]

def initial_state(m: int = 3, k: int = 3) -> dict:
    grid = [[None for _ in range(m)] for _ in range(m)]
    return {"grid": grid, "m": m, "k": k, "to_move": "X"}

def copy_state(state: dict) -> dict:
    return {"grid":[row[:] for row in state["grid"]],"m":state["m"],"k":state["k"],"to_move":state["to_move"]}

def pretty_print(state: dict):
    m = state["m"]
    for r in range(m):
        print(" ".join("." if c is None else c for c in state["grid"][r]))
    print("To move:", state["to_move"])
