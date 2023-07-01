def find_items_backpack(items, max_weight):
    valid_combinations = []
    backtrack(items, max_weight, [], valid_combinations)
    return valid_combinations


def backtrack(items, max_weight, current_combination, valid_combinations):
    if max_weight < 0:
        return
    if max_weight == 0:
        valid_combinations.append(current_combination)
        return
    for i in range(len(items)):
        item = items[i]
        remaining_items = items[i + 1:]
        if item[1] <= max_weight:
            backtrack(remaining_items, max_weight - item[1], current_combination + [item], valid_combinations)


items = {
    'Тент': 2,
    'Спальник': 1,
    'Фонарик': 0.5,
    'Палатка': 3,
    'Еда': 2,
    'Вода': 1.5
}
max_weight = 5
result = find_items_backpack(list(items.items()), max_weight)
for combination in result:
    print(combination)
