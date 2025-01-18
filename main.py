from config import MOVIE_JSON, menu_list
from menu import Menu
from movie_library import MovieLibrary

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""

    def __init__(self) -> None:
        super().__init__("Error: Please enter a positive number!")

def main() -> None:
    """Run the Movie Library Application"""

    movie_library = MovieLibrary(MOVIE_JSON)
    menu = Menu(movie_library)

    while True:
        menu.show_menu()
        user_input = input("\nChoose an option: ").strip()

        try:
            user_choice = int(user_input)-1

            if user_choice < 0:
                raise NegativeNumberError

            menu_key = list(menu_list.keys())[user_choice]
            menu_title = list(menu_list.values())[user_choice]
            method_name = f"menu_{menu_key}"
            method = getattr(menu, method_name)

            print(f"- - - - - - - - - {menu_title} - - - - - - - - - ")

            method()

        except NegativeNumberError as e:
            print(e)
        except ValueError:
            print("Error: Please enter a valid numeric value.")
        except IndexError:
            print(f"Error: Please select a valid option (1 to {len(menu_list)}).")
        except movie_library.MovieNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__} - {e}")

if __name__ == "__main__":
    main()
