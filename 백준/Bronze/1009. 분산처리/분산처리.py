def last_computer(a, b):
    cycle = []
    current = a % 10
    while current not in cycle:
        cycle.append(current)
        current = (current * a) % 10
    
    cycle_length = len(cycle)
    index = (b - 1) % cycle_length
    return cycle[index] if cycle[index] != 0 else 10

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(last_computer(a, b))
