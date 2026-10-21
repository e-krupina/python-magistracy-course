trainer_last_name = input("Ваша фамилия (например, Смирнов): ")
trainer_first_name = input("Ваше имя (например, Андрей): ")
print(f"Здравствуйте, {trainer_first_name}! Начинаем зачёт")

number_of_athletes = int(
    input("\nКоличество спортсменов — целое положительное число (например, 3): ")
)
number_of_sets = int(
    input("Количество подходов — целое положительное число (например, 3): ")
)

athlete_surnames = []
pull_up_totals = []
successful_athletes = 0

for athlete_index in range(number_of_athletes):
    print(f"\n--- Спортсмен {athlete_index + 1} ---")
    athlete_surname = input("Фамилия спортсмена (например, Петров): ")
    set_results = []

    for set_index in range(number_of_sets):
        result = int(
            input(
                f"Подход {set_index + 1} — число подтягиваний (целое неотрицательное, например 10): "
            )
        )
        set_results.append(result)

    total = sum(set_results)
    athlete_surnames.append(athlete_surname)
    pull_up_totals.append(total)

    standard_result = "не выполнен"
    if total >= 30:
        standard_result = "выполнен"
        successful_athletes += 1
    print(f"{athlete_surname}: всего {total} — норматив {standard_result}")

print("\nИтоговая таблица:")
for index in range(len(athlete_surnames)):
    row_number = index + 1
    print(f"{row_number}. {athlete_surnames[index]} — {pull_up_totals[index]}")

group_total = sum(pull_up_totals)
print(f"\nНорматив выполнили: {successful_athletes} из {number_of_athletes}")
print(f"Всего подтягиваний группы: {group_total}")
print(f"До свидания, {trainer_first_name}!")
