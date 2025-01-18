class Movie:
    """Represents a movie with its title, director, year and genres."""

    def __init__(
            self,
            title: str,
            director: str,
            year: int,
            genres: list[str],
    ):
        """Initialize a new Movie instance.

        :param title (str): The title of the movie.
        :param director (str): The director of the movie.
        :param year (int): The year of the movie.
        :param genres (list): The genres of the movie.
        """
        self.title = title
        self.director = director
        self.year = year
        self.genres = genres

    def __str__(self):
        """Returns a string representation of a Movie."""
        return f"{self.title} - {self.director} - {self.year} - {', '.join(self.genres)}"

    def as_list(self) -> list[str]:
        """Converts the movie details into a list of strings."""
        return [self.title, self.director, self.year, ", ".join(self.genres)]
