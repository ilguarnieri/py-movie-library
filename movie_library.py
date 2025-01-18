import json
from movie import Movie

class MovieLibrary:
    """A class to manage a library of movies stored in a JSON file."""

    def __init__(self, json_file: str) -> None:
        """Initialize a new Movie Library instance.

        :param json_file (str): Path to the JSON file.
        :raises FileNotFoundError: If the JSON file does not exist.
        """
        self.json_file = json_file
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                __movies_data = json.load(file)
                self.movies = [Movie(**movie) for movie in __movies_data]
        except FileNotFoundError:
            error_msg = f"File '{self.json_file}' not found"
            raise FileNotFoundError(error_msg) from None

    def __update_json_file(self) -> None:
        """Update the JSON file with the current state of the movies list."""
        with open(self.json_file, "w", encoding="utf-8") as file:
            serialized_film = [movie.__dict__ for movie in self.movies]
            json.dump(serialized_film, file, indent=4, ensure_ascii=False)

    def get_movies(self) -> list[list[str]]:
        """Retrive a list of all movies in the collection."""
        return [movie.as_list() for movie in self.movies]

    def add_movie(
            self,
            title: str,
            director: str,
            year: int,
            genres: list[str],
    ) -> None:
        """Add a new movie to the library.

        :param title: The title of the movie.
        :param director: The director of the movie.
        :param year: The release year of the movie.
        :param genres: A list of genres of the movie.
        """
        new_movie = Movie(title, director, year, genres)
        self.movies.append(new_movie)
        self.__update_json_file()

    def remove_movie(self, title: str) -> Movie:
        """Remove a movie from the library.

        :param title: The title of the movie.
        :return Movie: The removed movie.
        :raises MovieNotFoundError: If the movie with the specified title
        does not exist.
        """
        found_movie = self.get_movie_by_title(title)
        if not found_movie:
            raise self.MovieNotFoundError

        self.movies.remove(found_movie)
        self.__update_json_file()
        return found_movie

    def update_movie(
            self,
            title: str,
            director: str = None,
            year: int = None,
            genres: list[str] = None,
    ) -> Movie:
        """Update a movie from the library.

        :param title: The title of the movie to update.
        :param director: Optional the new director of the movie.
        :param year: Optional the new release year of the movie.
        :param genres: Optional the new genres of the movie.
        :return: Movie: The updated movie.
        :raises MovieNotFoundError: If the movie with the specified title
        does not exist.
        """
        found_movie = self.get_movie_by_title(title)
        if not found_movie:
            raise self.MovieNotFoundError

        if director:
            found_movie.director = director
        if year:
            found_movie.year = year
        if genres:
            found_movie.genres = genres
        self.__update_json_file()
        return found_movie

    def get_movie_titles(self) -> list[str]:
        """Retrive a list of all movie titles."""
        return [movie.title for movie in self.movies]

    def count_movies(self) -> int:
        """Retrive the total number of movies."""
        return len(self.movies)

    def get_movie_by_title(self, title: str) -> Movie:
        """Retrive the movie with the corresponding name.

        :param title: the title of the movie.
        :return: Movie: the object matching the given title.
        :raises MovieNotFoundError: If the movie with the specified title
        """
        for movie in self.movies:
            if movie.title.lower() == title.lower().strip():
                return movie
        raise self.MovieNotFoundError

    def get_movies_by_title_substring(self, substring: str) -> list[list[str]]:
        """Retrive all movies that contain the substring in their title.

        :param substring: The substring to search for in movie titles.
        :return: A list of movie.
        """
        return [
            movie.as_list()
            for movie in self.movies
            if substring.strip() in movie.title
        ]

    def get_movies_by_year(self, year: int) -> list[list[str]]:
        """Retrieve all movies released in a specific year.

        :param year: The release year to filter movies by.
        :return: A list of movie.
        """
        return [
            movie.as_list()
            for movie in self.movies
            if movie.year == year
        ]

    def count_movies_by_director(self, director: str) -> int:
        """Count the number of movies directed by a specific director.

        :param director: The name of the director to filter movies by.
        :return: The number of movies.
        """
        return len([
            movie
            for movie in self.movies
            if movie.director.lower() == director.lower().strip()
        ])

    def get_movies_by_genre(self, genre: str) -> list[list[str]]:
        """Retrieve all movies that belong to a specific genre.

        :param genre: The genre to filter movies by.
        :return: A list of movie.
        """
        temporary_list = []
        for movie in self.movies:
            for movie_genre in movie.genres:
                if movie_genre.lower() == genre.lower().strip():
                    temporary_list.append(movie.as_list())
        return temporary_list

    def get_oldest_movie_title(self) -> str:
        """Retrieve the oldest movie title."""
        oldest_movie = min(self.movies, key=lambda movie: movie.year)
        return oldest_movie.title

    def get_average_release_year(self) -> float:
        """Calculate the average release year of all movie."""
        sum_years = sum(movie.year for movie in self.movies)
        average = sum_years / len(self.movies)
        return round(average, 2)

    def get_longest_title(self) -> str:
        """Retrieve the longest movie title."""
        longest_title_movie = max(
            self.movies, key=lambda movie: len(movie.title),
        )
        return longest_title_movie.title

    def get_titles_between_years(
            self,
            start_year: int,
            end_year: int,
    ) -> list[str]:
        """Retrieve all titles between two years.

        :param start_year: The start year of the range.
        :param end_year: The end year of the range.
        :return: A list of movie titles released within the range.
        """
        return [
            movie.title
            for movie in self.movies
            if start_year <= movie.year <= end_year
        ]

    def get_most_common_year(self) -> int:
        """Find the most common release year among all movies."""
        years_count = {}
        for movie in self.movies:
            year = movie.year
            if year in years_count:
                years_count[year] += 1
            else:
                years_count[year] = 1
        return max(years_count, key=years_count.get)

    class MovieNotFoundError(Exception):
        """Custom excetion raised when a movie is not found."""

        def __init__(self):
            super().__init__("Movie was not found")
