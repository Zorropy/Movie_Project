import statistics as stats
import random


def get_user_rating():
    while True:
        try:
            rating_input = float(input("Enter new movie rating (0-10): "))
            if not 0 <= rating_input <= 10:
                raise ValueError
            return rating_input
        except ValueError:
            print("Error. Please enter a number between 0-10")


def exit_program(movies):
    print("Bye!!!")
    exit()


def list_movies(movies):
    print(f"{len(movies)} movies in total")
    for title, rating in movies.items():
        print(f"{title}: {rating}")


def add_movie(movies):
    title_input = input("Enter new movie name: ").title()
    if not title_input.strip():
        print("A movie name must be provided.")
        return
    if title_input in movies:
        print(f"Movie {title_input} already exists!")

    rating_input = get_user_rating()
    movies[title_input] = rating_input
    print(f"Movie {title_input} successfully added")


def delete_movie(movies):
    movie_input = input("Enter a movie name to delete: ").title()
    if movie_input not in movies:
        print(f"Movie {movie_input} doesn't exist!")
        return
    movies.pop(movie_input)
    print(f"Movie {movie_input} successfully deleted")


def update_movie(movies):
    title_input = input("Enter movie name: ").title()
    if title_input not in movies:
        print(f"Movie {title_input} doesn't exist!")
        return
    rating_input = get_user_rating()
    movies.update({title_input: rating_input})
    print(f"Movie {title_input} successfully updated")


def movie_stats(movies):
    average_rating(movies)
    median_rating(movies)
    best_movie(movies)
    worst_movie(movies)


def average_rating(movies):
    average = round(sum(movies.values()) / len(movies), 2)
    print(f"Average rating: {average}")
    print()


def median_rating(movies):
    median = stats.median(movies.values())
    print(f"Median rating: {median}")
    print()


def best_movie(movies):
    best_rating = sorted(movies.values(), reverse=True)[0]
    print("Best movie(s):")
    for title, rating in movies.items():
        if best_rating == rating:
            print(f"{title}: {rating}")
    print()


def worst_movie(movies):
    worst_rating = sorted(movies.values())[0]
    print("Worst movie(s):")
    for title, rating in movies.items():
        if worst_rating == rating:
            print(f"{title}: {rating}")
    print()


def random_movie(movies):
    if not movies:
        print("No movies available.")
        return
    title, rating = random.choice(list(movies.items()))
    print(f"Your random movie for tonight: {title} (Rating: {rating})")


def search_movie(movies):
    search_input = input("Please enter movie name to search: ").strip().lower()
    if not search_input:
        return
    movie_found = False
    for movie in movies:
        if search_input in movie.lower():
            print(f"{movie}: {movies[movie]}")
            movie_found = True
    if not movie_found:
        print(f"No movies found for '{search_input}'")


def sort_movies(movies):
    sorted_movies = dict(sorted(movies.items(), key=lambda x: x[1], reverse=True))
    for title, rating in sorted_movies.items():
        print(f"{title}: {rating}")


def main():
    func_dict = {0: exit_program,
                 1: list_movies,
                 2: add_movie,
                 3: delete_movie,
                 4: update_movie,
                 5: movie_stats,
                 6: random_movie,
                 7: search_movie,
                 8: sort_movies}
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }
    while True:
        print("""********** My Movies Database **********

Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
0. Exit

Enter choice (0-8): """, end="")
        try:
            user_input = int(input())
            if not 0 <= user_input <= 8:
                raise ValueError
            func_dict[user_input](movies)
        except ValueError:
            print("Error. Please choose a number between 0-8.")

        print()
        input("Press enter to continue...")


if __name__ == "__main__":
    main()
