starting_number = int(input())
bonus_points = 0

if starting_number <= 100:
    bonus_points = 5
elif starting_number <= 1000:
    bonus_points = starting_number * 0.20
elif starting_number > 1000:
    bonus_points = starting_number * 0.10

if starting_number % 2 == 0:
    bonus_points = bonus_points + 1
elif starting_number % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(bonus_points + starting_number)
