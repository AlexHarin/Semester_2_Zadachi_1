def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
a = int(input("Введите начало интервала (a): "))
b = int(input("Введите конец интервала (b): "))
sum_of_primes = 0
for number in range(a, b + 1):
    if is_prime(number):
        sum_of_primes += number
print(f"Сумма простых чисел в интервале от {a} до {b} равна: {sum_of_primes}")