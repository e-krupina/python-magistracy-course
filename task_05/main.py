host_name = input("Ваше имя (например, Ольга): ")
print(f"Здравствуйте, {host_name}! Начинаем голосование")

festival_movies = ("дюна", "аватар", "матрица", "интерстеллар", "шрек")
available_movies = set(festival_movies)
vote_counts = dict.fromkeys(festival_movies, 0)
voted_names = set()
all_viewers_choices = []

print("Фильмы в программе фестиваля:", ", ".join(festival_movies))

viewer_name = input('\nИмя зрителя, например Аня (или "стоп"): ').strip()
while viewer_name.lower() != "стоп":
    normalized_name = viewer_name.lower()

    if normalized_name in voted_names:
        print(f"{viewer_name}, вы уже голосовали, второй голос не засчитан")
    else:
        voted_names.add(normalized_name)
        entered_movies = input(
            "Выберите через запятую: дюна, аватар, матрица, интерстеллар, шрек: "
        )
        selected_movies = set()

        for entered_movie in entered_movies.split(","):
            normalized_movie = entered_movie.strip().lower()
            if normalized_movie in available_movies:
                selected_movies.add(normalized_movie)
            elif normalized_movie:
                print(f"Фильма «{normalized_movie}» нет в программе, голос не засчитан")

        for selected_movie in selected_movies:
            vote_counts[selected_movie] += 1

        all_viewers_choices.append(selected_movies)
        print(f"Спасибо, {viewer_name}! Засчитано голосов: {len(selected_movies)}")

    viewer_name = input('\nИмя зрителя, например Аня (или "стоп"): ').strip()

print("\nИтоги голосования")
print(f"Проголосовало зрителей: {len(voted_names)}")
for movie in festival_movies:
    print(f"{movie} - {vote_counts[movie]}")

winner = festival_movies[0]
for movie in festival_movies[1:]:
    if vote_counts[movie] > vote_counts[winner]:
        winner = movie
print(f"Победитель: {winner} ({vote_counts[winner]})")

if all_viewers_choices:
    liked_by_all = set.intersection(*all_viewers_choices)
else:
    liked_by_all = set()

if liked_by_all:
    ordered_common = [movie for movie in festival_movies if movie in liked_by_all]
    print("Понравились всем:", ", ".join(ordered_common))
else:
    print("Фильмов, понравившихся всем, нет")

never_selected = available_movies - set().union(*all_viewers_choices) if all_viewers_choices else available_movies
ordered_never_selected = [movie for movie in festival_movies if movie in never_selected]
print("Не выбрал никто:", ", ".join(ordered_never_selected) or "таких фильмов нет")
print(f"До свидания, {host_name}!")
