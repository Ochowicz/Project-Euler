fibbonaci = [1,1]
while (fibbonaci[-1] + fibbonaci[-2]) < 4000000:
    fibbonaci.append(fibbonaci[-1] + fibbonaci[-2])
print(fibbonaci)

even_fibbonaci = []
for number in fibbonaci:
    if number % 2 == 0:
        even_fibbonaci.append(number)

sum_even_fibbonaci = 0
for num in even_fibbonaci:
    sum_even_fibbonaci += num

print(sum_even_fibbonaci)
