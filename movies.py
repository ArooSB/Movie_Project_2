import random
import movie_storage
import omdb_api

API_KEY = "b489c489"


def list_movies():
    movies = movie_storage.get_movies()
    print(len(movies), "movies in total")
    for movie, details in movies.items():
        print(f"{movie}: {details['year']} - Rating: {details['rating']}")


def add_movies():
    title = input("Add a movie name: ")
    if title in movie_storage.get_movies():
        print("In the list")
        return
    else:
        details = omdb_api.fetch_movie_details(API_KEY, title)
        if details and "Year" in details and "imdbRating" in details:
            year = details["Year"]
            rating = float(details["imdbRating"])
            movie_storage.add_movie(title, year, rating)
            list_movies()
        else:
            print("Movie not found in OMDb")


def delete_movies():
    title = input("Delete a movie: ")
    movie_storage.delete_movie(title)
    list_movies()


def search_movie():
    query = input("Enter movie name: ").lower()
    movies = movie_storage.get_movies()
    matching_movies = [
        (movie, details["rating"])
        for movie, details in movies.items()
        if query in movie.lower()
    ]
    for movie, rating in matching_movies:
        print(movie + ",", rating)


def update_movie():
    title = input("Enter movie name: ")
    if title not in movie_storage.get_movies():
        print("Movie not found.")
    else:
        rating = input("Enter new rating: ")
        movie_storage.update_movie(title, float(rating))
        print(f"The rating for '{title}' has been updated to {rating}.")


def average_movie_rating():
    movies = movie_storage.get_movies()
    total_rating = sum(details["rating"] for details in movies.values())
    average_rating = total_rating / len(movies)
    print(f"The average rating: {average_rating:.2f}")
    return average_rating


def calculate_median_rating():
    movies = movie_storage.get_movies()
    sorted_ratings = sorted(details["rating"] for details in movies.values())
    num_ratings = len(sorted_ratings)
    if num_ratings % 2 == 0:
        mid_index = num_ratings // 2
        median_rating = (sorted_ratings[mid_index - 1] + sorted_ratings[mid_index]) / 2
    else:
        mid_index = num_ratings // 2
        median_rating = sorted_ratings[mid_index]
    print(f"The median rating is: {median_rating:.2f}")
    return median_rating


def best_rating():
    movies = movie_storage.get_movies()
    max_rating = max(details["rating"] for details in movies.values())
    best_movies = [
        movie for movie, details in movies.items() if details["rating"] == max_rating
    ]
    print(f"The best movie(s): {best_movies}, with rating {max_rating}")
    return best_movies, max_rating


def worst_rating():
    movies = movie_storage.get_movies()
    min_rating = min(details["rating"] for details in movies.values())
    worst_movies = [
        movie for movie, details in movies.items() if details["rating"] == min_rating
    ]
    print(f"The worst movie(s): {worst_movies}, with rating {min_rating}")
    return worst_movies, min_rating


def random_movie():
    movies = movie_storage.get_movies()
    movie_name, details = random.choice(list(movies.items()))
    print(
        f"Random movie: {movie_name} - Year: {details['year']} - Rating: {details['rating']:.1f}"
    )


def main():
    while True:
        print(
            "Select options:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Search movie\n5. Update movie\n6. Average rating\n7. Median rating\n8. Best rating\n9. Worst rating\n10. Random movie"
        )
        action = input("Enter choice (0-10): ")
        if action == "0":
            print("Bye!")
            break
        elif action == "1":
            list_movies()
        elif action == "2":
            add_movies()
        elif action == "3":
            delete_movies()
        elif action == "4":
            search_movie()
        elif action == "5":
            update_movie()
        elif action == "6":
            average_movie_rating()
        elif action == "7":
            calculate_median_rating()
        elif action == "8":
            best_rating()
        elif action == "9":
            worst_rating()
        elif action == "10":
            random_movie()
        else:
            print("Invalid option!")
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
