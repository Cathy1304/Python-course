K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_shifts = []
count = 0

print("Cannot change the same player.")
for i in range(K, 9):
    for j in range(9, L - 1, -1):
        for k in range(M, 9):
            for l in range(9, N - 1, -1):

                if i % 2 == 0 and j % 2 != 0 and k % 2 == 0 and l % 2 != 0:

                    if i != k or j != l:

                        valid_shifts.append(f"{i}{j} - {k}{l}")

                        count += 1
                        if count == 6:
                          break

if len(valid_shifts) == 0:
    print("Cannot change the same player.")
else:
    for shift in valid_shifts:
        print(shift)
