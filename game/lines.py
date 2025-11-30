def lines(m: int, k: int):
    for r in range(m):
        for s in range(m-k+1):
            yield [(r,s+i) for i in range(k)]
    for c in range(m):
        for s in range(m-k+1):
            yield [(s+i,c) for i in range(k)]
    for r in range(m-k+1):
        for c in range(m-k+1):
            yield [(r+i,c+i) for i in range(k)]
    for r in range(m-k+1):
        for c in range(k-1,m):
            yield [(r+i,c-i) for i in range(k)]
