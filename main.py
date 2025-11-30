from game.state import initial_state,pretty_print
from search.alphabeta import minimax_ab

if __name__ == "__main__":
    s=initial_state(3,3)
    pretty_print(s)
    mv=minimax_ab(s)
    print("Best move:",mv)
