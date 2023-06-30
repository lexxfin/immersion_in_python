def get_hex_string(number):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""
    if number == 0:
        return "0"
    while number > 0:
        remainder = number % 16
        hex_string = hex_digits[remainder] + hex_string
        number = number // 16
    return hex_string


num = int(input("Введите целое число: "))
hex_string = get_hex_string(num)
if hex_string == hex(num)[2:].upper():
    print(f"Десятичное число {num} в шестнадцатиричном формате {hex_string}")
