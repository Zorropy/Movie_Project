def exit_program(movies):
    print("Bye!!!")
    exit()


def main():
    func_dict = {0: exit_program}
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

        input("Press enter to continue...")


if __name__ == "__main__":
    main()
