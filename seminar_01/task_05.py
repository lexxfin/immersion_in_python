import random

number = random.randint(0, 1001)
attempts = 1
print("Угадайте число от 0 до 1000. У вас 10 попыток")
while attempts < 11:
    guess = int(input(f"{attempts} попытка, введите число: "))
    if guess == number:
        print(f"Поздравляем! Вы угадали число за {attempts} попыток")
        break
    elif guess < number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    attempts += 1
if attempts == 11:
    print("Вы проиграли. Загаданное число было", number)
