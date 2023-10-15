start = int(input())
final = int(input())
magic_number = int(input())
combination_is_found = False
counter_of_combinations = 0
for i in range(start, final + 1):
    for j in range(start, final + 1):
        counter_of_combinations += 1
        if i + j == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
   print(f"Combination N:{counter_of_combinations} ({i} + {j} = {magic_number})")
else:
    print(f"{counter_of_combinations} combinations - neither equals {magic_number}")

