from config import menu_list
from datetime import datetime
from tabulate import tabulate

current_year = datetime.now().year
EMPTY_COLL_MSG = "🥲 Empty collection. Add a movie!"
NO_RESULTS_MSG = "🥲 I'm sorry, the search did not return any results."

class Menu:
    """Class to manage the user inferface."""

    def __init__(self, movie_library) -> None:
        """Initialize the Menu object.

        :param movie_library: An instance of the MovieLibrary class to manage the collection.
        """
        self.movie_library = movie_library

    def show_menu(self) -> None:
        """Show the program menu."""

        print("\nMENÙ")
        for i, (_key, _value) in enumerate(menu_list.items(), start=1):
            print(f"{i}. {_value}")

    def movie_table(self, movie_list: list) -> str:
        """Format a list of movie as a table.

        :param movie_list: A list of movies details.
        :return: A formatted table.
        """
        headers = ["Title", "Director", "Year", "Genres"]
        return tabulate(movie_list, headers=headers)

    def menu_add_movie(self) -> None:
        """This method asks title, director, year and genres to add a new film to the collection.

        :returns: None if the input year is not valid
        """
        title = input("Title: ").strip().capitalize()
        director = input("Director: ").strip().capitalize()
        year = int(input("Release year: ").strip())
        genres_input = input("Genres (comma-separated): ").split(",")
        genres = [genre.strip().capitalize() for genre in genres_input]

        if not 1000 < year < current_year:
            print(f"Error: the year {year} is not valid!")
            return None

        self.movie_library.add_movie(title, director, year, genres)
        print("\n🥳 Movie added!")

    def menu_update_movie(self) -> None:
        """This method asks the user for a movie title and the new details
        (director, year, genres) to update.

        :returns: None if the input year is not valid
        """
        title = input("Title of the movie to update: ").strip().capitalize()
        director = input("New director (press Enter to keep unchanged): ").strip().capitalize() or None
        year = input("New release year (press Enter to keep unchanged): ").strip()
        if year:
            year = int(year)
            if not 1000 < year < current_year:
                print(f"Error: the year {year} is not valid!")
                return None

        genres_input = input("New genres (comma-separated, press Enter to keep unchanged): ").strip()
        if genres_input:
            genres = [genre.strip().capitalize() for genre in genres_input.split(",")]
            movie = self.movie_library.update_movie(title, director, year, genres)
        else:
            movie = self.movie_library.update_movie(title, director, year)
        print(f"✏️ Movie successfully updated\n{movie}")

    def menu_delete_movie(self) -> None:
        """Prompt the user to delete a movie from the collection by title."""
        title = input("Title of the movie to delete: ").strip()
        movie = self.movie_library.remove_movie(title)
        print(f"🗑️ Movie successfully deleted!\n{movie}")

    def menu_search_by_title(self) -> None:
        """Prompt the user to search for a movie by title."""
        title = input("Title of the movie to search: ").strip()
        movie = self.movie_library.get_movie_by_title(title)
        if movie:
            print(f"\n{movie}")
        else:
            print("🥲 Sorry movie not found")

    def menu_search_part_title(self) -> None:
        """Prompt the user to search for a movies containing part of a title."""
        title = input("Part of the title of the movie to search: ").strip()
        movie_list = self.movie_library.get_movies_by_title_substring(title)
        if movie_list:
            print(self.movie_table(movie_list))
        else:
            print(NO_RESULTS_MSG)

    def menu_search_by_year(self) -> None:
        """Prompt the user to search for a movies by year.

        :returns: None if the input year is not valid
        """
        year = int(input("Movie release year: ").strip())
        if not 1000 < year < current_year:
            print(f"Error: the year {year} is not valid!")
            return None
        movie_list = self.movie_library.get_movies_by_year(year)
        if movie_list:
            print(self.movie_table(movie_list))
        else:
            print(NO_RESULTS_MSG)

    def menu_search_by_genre(self) -> None:
        """Prompt the user to search for a movies by genre."""
        genres = input("Movies genre : ").strip()
        movie_list =  self.movie_library.get_movies_by_genre(genres)
        if movie_list:
            print(self.movie_table(movie_list))
        else:
            print(NO_RESULTS_MSG)

    def menu_movie_between_year(self) -> None:
        """Prompt the user to search for a movies titles between two years."""
        start_year = int(input("Start year: ").strip())
        end_year = int(input("End year: ").strip())
        title_list =  self.movie_library.get_titles_between_years(start_year, end_year)
        if title_list:
            for title in title_list:
                print(title)
        else:
            print(NO_RESULTS_MSG)

    def menu_count_movies(self) -> None:
        """Display the total number of movies in the collection."""
        count_movies = self.movie_library.count_movies()
        if count_movies:
            print(count_movies)
        else:
            print(EMPTY_COLL_MSG)

    def menu_view_all_title(self) -> None:
        """Display all movies title in the collection."""
        title_list = self.movie_library.get_movie_titles()
        if title_list:
            for title in title_list:
                print(title)
        else:
            print(EMPTY_COLL_MSG)

    def menu_view_all_movie(self) -> None:
        """Display all movies in the collection."""
        movie_list = self.movie_library.get_movies()
        if movie_list:
            print(self.movie_table(movie_list))
        else:
            print(EMPTY_COLL_MSG)

    def menu_oldest_movie(self) -> None:
        """Display the title of the oldest movie in the collection."""
        movie = self.movie_library.get_oldest_movie_title()
        if movie:
            print(movie)
        else:
            print(EMPTY_COLL_MSG)

    def menu_average_year(self) -> None:
        """Display the average release year of the all movies in the collection."""
        average = self.movie_library.get_average_release_year()
        if average:
            print(average)
        else:
            print(EMPTY_COLL_MSG)

    def menu_longest_title(self) -> None:
        """Display the movie with the longest title in the collection."""
        title = self.movie_library.get_longest_title()
        if title:
            print(title)
        else:
            print(EMPTY_COLL_MSG)

    def menu_common_year(self) -> None:
        """Display the common year of the movies in the collection."""
        year = self.movie_library.get_most_common_year()
        if year:
            print(year)
        else:
            print(EMPTY_COLL_MSG)

    def menu_count_by_director(self) -> None:
        """Display the total number of movies by director in the collection."""
        director = input("Director: ").strip()
        numbers_movie = self.movie_library.count_movies_by_director(director)
        if numbers_movie:
            print(numbers_movie)
        else:
            print(NO_RESULTS_MSG)

    def menu_exit(self) -> None:
        """Exit the application."""
        print("Goodbye!")
        exit(1)
