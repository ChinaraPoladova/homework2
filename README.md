
# Generalized Tic-Tac-Toe AI Project

This project implements a generalized m×m, k-in-a-row Tic-Tac-Toe AI with:
- Game engine (rules, winner detection, utility)
- Full Minimax (3×3)
- Alpha-Beta pruning (with move ordering)
- Depth-limited search + heuristic for m>3
- Deterministic tie-breaking
- Tests (pytest)
- Performance measurement script

## Run demo
```
python main.py
```

## Run tests
```
pip install pytest
pytest -q
```

## Performance
Run:
```
python performance.py
```
This produces `perf_results.json`.
