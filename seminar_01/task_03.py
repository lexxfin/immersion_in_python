num = int(input("Введите число: "))

if num < 2 or num > 100000:
    print("Число должно быть в диапазоне от 2 до 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print(f"{num} является {('составным', 'простым')[is_prime]} числом")
