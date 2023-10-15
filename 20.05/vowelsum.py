some_string = input()
sum_of_points = 0
for charater in some_string:
    if charater == "a":
        sum_of_points += 1
    elif charater == "e":
        sum_of_points += 2
    elif charater == "i":
        sum_of_points += 3
    elif charater == "o":
        sum_of_points += 4
    elif charater == "u":
        sum_of_points += 5
print(sum_of_points)