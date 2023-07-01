from collections import Counter


def get_duplicate_elements(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


input_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
result_list = get_duplicate_elements(input_list)
print("Список с повторяющимися элементами: ", result_list)
