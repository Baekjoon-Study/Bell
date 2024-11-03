
N = int(input()) 
filenames = [input().strip() for _ in range(N)]  
length = len(filenames[0])
pattern = []

for i in range(length):
    current_char = filenames[0][i]
    is_same = True
    for j in range(1, N):
        if filenames[j][i] != current_char:
            is_same = False
            break
    if is_same:
        pattern.append(current_char)
    else:
        pattern.append('?')

print("".join(pattern))
