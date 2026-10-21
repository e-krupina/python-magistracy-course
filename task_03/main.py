employee_surname = input("Фамилия сотрудника (например, Кузнецова): ")
employee_name = input("Имя сотрудника (например, Ольга): ")
print(f"Здравствуйте, {employee_name}! Приём заявок открыт")

reviewed = 0
enrolled = 0
applicant_surname = input(
    '\nФамилия абитуриента, например Петров (или "завершить"): '
).strip()

while applicant_surname.lower() != "завершить":
    points = int(input("Балл абитуриента — целое число (например, 235): "))
    olympiad_answer = input("Диплом олимпиады — только «да» или «нет»: ").strip().lower()

    reviewed += 1
    passed_by_score = points >= 220
    passed_by_olympiad = olympiad_answer == "да" and points >= 180

    if passed_by_score or passed_by_olympiad:
        enrolled += 1
        decision = "одобрена"
    else:
        decision = "отклонена"

    print(f"{applicant_surname}: заявка {decision}")
    applicant_surname = input(
        '\nФамилия абитуриента, например Петров (или "завершить"): '
    ).strip()

print(f"\nРассмотрено абитуриентов: {reviewed}")
print(f"Зачислено: {enrolled}")
print(f"До свидания, {employee_name}!")
