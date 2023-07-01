def find_common_belongings(friends):
    common_belongings = set.intersection(*friends.values())
    unique_belongings = {}
    for friend, belongings in friends.items():
        unique_belongings[friend] = set(belongings) - common_belongings
    missing_belongings = {}
    for friend, belongings in friends.items():
        missing_belongings[friend] = common_belongings - set(belongings)
    return common_belongings, unique_belongings, missing_belongings


num_friends = int(input("Введите количество друзей: "))
friends = {}
for i in range(num_friends):
    name = input(f"Введите имя {i + 1} друга: ")
    belongings = input(f"Введите личные вещи {i + 1} друга (разделенные пробелами): ").split()
    friends[name] = tuple(belongings)
common, unique, missing = find_common_belongings(friends)
print("Вещи, которые есть у всех друзей: ", common)
for friend, belongings in unique.items():
    print(f"Уникальные вещи для {friend}: {belongings}")
for friend, belongings in missing.items():
    print(f"Вещи, которые есть у всех друзей, за исключением {friend}: {belongings}")
