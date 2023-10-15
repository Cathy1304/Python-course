

first_num_first_digit_start = int(input())
first_num_second_digit_start = int(input())
second_num_first_digit_start = int(input())
second_num_second_digit_start = int(input())
counter = 0
has_ended = False

for first_num_first_dig in range(first_num_first_digit_start, 9):
    for first_num_second_dig in range(9, first_num_second_digit_start - 1, -1):
        for second_num_first_dig in range(second_num_first_digit_start, 9):
            for second_num_second_dig in range(9, second_num_second_digit_start - 1, -1):
                is_valid = first_num_first_dig % 2 == 0 and \
                    second_num_first_dig % 2 == 0 and \
                    first_num_second_dig % 2 != 0 and \
                    second_num_second_dig % 2 != 0

                first_num = first_num_first_dig * 10 + first_num_second_dig
                second_num = second_num_first_dig * 10 + second_num_second_dig

                if is_valid and first_num == second_num:
                    print("Cannot change the same player.")
                elif is_valid and first_num != second_num:
                    print(f"{first_num} - {second_num}")
                    counter += 1
                if counter >= 6:
                    has_ended = True
                if has_ended:
                    break
            if has_ended:
                break
        if has_ended:
            break
    if has_ended:
        break
