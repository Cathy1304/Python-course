countNumbers = int(input())

biggestNum = float('-inf')
smallestNum = float('inf')

for i in range(countNumbers):
    number = int(input())
    if biggestNum < number:
        biggestNum = number
    if smallestNum > number:
        smallestNum = number

print(f'Max number: {biggestNum}')
print(f'Min number: {smallestNum}')