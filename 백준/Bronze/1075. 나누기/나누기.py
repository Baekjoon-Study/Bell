
N = int(input().strip())
F = int(input().strip())
N = (N // 100) * 100

for i in range(100):
    if (N + i) % F == 0:
        print(f"{i:02d}")
        break
