
# Report: Design, Heuristic, and Performance

## Design choices
- State represented as dict: `{"grid", "m", "k", "to_move"}` for simplicity and picklability.
- Deterministic tie-breaking via lexicographic move ordering.
- Move ordering uses a shallow heuristic probe (evaluate resulting state) to improve pruning.

## Heuristic
- For every k-length window (rows, cols, diagonals):
  - If both X and O present -> blocked, score 0.
  - Else if X has t pieces -> +10^(t-1)
  - Else if O has t pieces -> -10^(t-1)
- Terminal states are given ±1000 to dominate heuristic.

## Pruning effectiveness
We instrumented node counters in minimax/alphabeta/depth-limited.
Run `python performance.py` to get node counts and times (saved to perf_results.json).

## Sample results (generated automatically when you run performance.py)
See `perf_results.json` for exact numbers.

