from fractions import Fraction


def calculate_fraction_operations(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)
    return fraction1 + fraction2, fraction1 * fraction2


fraction1 = input("Введите первую дробь (в формате 'a/b'): ")
fraction2 = input("Введите вторую дробь (в формате 'a/b'): ")
sum_result, product_result = calculate_fraction_operations(fraction1, fraction2)
print("Сумма дробей равна:", sum_result)
print("Произведение дробей равно:", product_result)
