all_numbers = range(1, 1000)
multiple_numbers = []
for number in all_numbers:
    if number % 3 == 0 or number % 5 == 0:
        multiple_numbers.append(number)
print(multiple_numbers)
sum_of_multiple_numbers = 0
for num in multiple_numbers:
    sum_of_multiple_numbers += num
print(sum_of_multiple_numbers)
