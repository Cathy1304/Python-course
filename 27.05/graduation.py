import sys

name = input()
current_year = 1
grade_total = 0
current_grade = 0
counter4 = 1

while current_year <= 12:
    current_grade = float(input())

    if current_grade >= 4:
        current_year += 1
    elif current_grade < 4:
        if counter4 >= 2:
            print(f'{name} has been excluded at {current_year} grade')
            sys.exit()
        counter4 += 1
    grade_total += current_grade

grade_total = grade_total / 12

if grade_total >= 4.00 and counter4 < 2:
    print(f'{name} graduated. Average grade: {grade_total:.2f}')