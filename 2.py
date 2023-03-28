import random



def tura(k: int, A, B, s: int):
    for i in range(s, A[k] - 1, -1):
        if B[i - A[k]] == True and B[i] != True:
            B[i] = True



def test(table):
    n = len(table)
    for s in range(1, 201):
        B = [False for i in range(0, s + 1)]
        B[0] = True
        for i in range(0, n):
            tura(i, table, B, s)
        if (B[len(B) - 1] != True): return False
    return True

index = 0
for _ in range(0, 100):
    while True:
        index += 1
        table = [
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20),

            random.randint(1, 80),
            random.randint(1, 80),
            random.randint(1, 80),
            random.randint(1, 80),
            random.randint(1, 80),
        ]
        result = test(table)
        if result == True:
            print(result, table, index)
            break

print('srednia', index / 100)