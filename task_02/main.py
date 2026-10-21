fio = input(
    "Введите фамилию, имя и отчество через пробел (например, Иванов Иван Иванович): "
).strip()
surname, name, patronymic = fio.split()
print("Рады вас видеть, " + name + "!")

products = []
product_examples = [
    ("первый", "яблоки"),
    ("второй", "хлеб"),
    ("третий", "молоко"),
]
for number, example in product_examples:
    products.append(input(f"Введите {number} товар — одно название (например, {example}): "))

print("Ваш список:", products)
print("Товаров в списке:", len(products))

products += ["стакан"]
print("Список после добавления подарка:", products)

sorted_products = sorted(products)
print("Отсортированный список:", sorted_products)

initials = name[0] + "." + patronymic[0] + "."
print(f"До свидания, {initials} {surname}!")
