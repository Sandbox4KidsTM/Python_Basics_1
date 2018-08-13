# While Loop Challenge 1
# Write a small program to count from 0 to 140 by 7.

num = 0
while num <= 140:
    print(num)
    num = num + 7
    
# While Loop Challenge 2
# Write a program to calculate the average of a list of numbers: [2.9, 5, 8.7, 15, 23, -10, 15, 8]
numbers = [2.9, 5, 8.7, 15, 23, -10, 15, 8]
idx = 0
total = 0
while idx < len(numbers):
    total = total + numbers[idx]
    idx = idx + 1
average = total / len(numbers)
