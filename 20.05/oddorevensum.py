n = int(input())

even_sum = 0
odd_sum = 0
for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even_sum += number
    elif i % 2 != 0:
        odd_sum += number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
elif even_sum != odd_sum:
    finsum = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {finsum}")