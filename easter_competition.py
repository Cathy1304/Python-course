easter_cakes = int(input())
best_result_name = ""
best_points = 0
for easter_cakes in range(easter_cakes):
    personal_points = 0
    cooker_name = input()
    command = input()
    while command != "Stop":
        easter_cake_value = int(command)
        personal_points += easter_cake_value
        command = input()
    print(f"{cooker_name} has {personal_points} points.")
    if personal_points > best_points:
        best_points = personal_points
        best_result_name = cooker_name
        print(f"{cooker_name} is the new number 1!")
print(f"{best_result_name} won competition with {best_points} points!")
