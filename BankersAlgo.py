def calculate_need(max_need, alloc, n, m):
    return [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
def all_safe_sequences(n, m, alloc, max_need, avail):
    need = calculate_need(max_need, alloc, n, m)
    finish = [False] * n
    sequence = []
    result = []
    def backtrack(work, finish, sequence):
        if len(sequence) == n:
            result.append(sequence[:])
            return
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                finish[i] = True
                sequence.append(i)
                backtrack(work, finish, sequence)
                for j in range(m):
                    work[j] -= alloc[i][j]
                finish[i] = False
                sequence.pop()
    backtrack(avail[:], finish, sequence)
    return result
n = 4
m = 3
alloc = [
    [1, 0, 1],
    [1, 1, 2],
    [1, 0, 3],
    [2, 0, 0]
]
max_need = [
    [4, 3, 1],
    [2, 1, 4],
    [1, 3, 3],
    [5, 4, 1]
]
avail = [3, 3, 0]
sequences = all_safe_sequences(n, m, alloc, max_need, avail)
if sequences:
    print(f"\nTotal Safe Sequences: {len(sequences)}")
    for seq in sequences:
        print(" -> ".join(f'P{i}' for i in seq))
else:
    print("No safe sequence exists.")
