fruits = {"apple": 5, "banana": 8, "grape": 2, "orange": 9}
lst = []
for fruit in fruits:
    if "e" in fruit:
        lst.append(fruit)
for key in lst:
    del fruits[key]
print(fruits)