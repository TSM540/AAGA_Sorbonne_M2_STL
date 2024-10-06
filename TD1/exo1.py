def von_neumann(seed):
    square = str(seed**2).zfill(20)
    middle = square[5:15]
    return int(middle)

def von_neumann_loop(seed, iterations=10):
    sequence = []
    current = seed
    for _ in range(iterations):
        current = von_neumann(current)
        sequence.append(current)
    return sequence

result = von_neumann_loop(1234567890, 10)
for i in result:
    print("-> "+ (str(i)))

# should consider rechecking the code