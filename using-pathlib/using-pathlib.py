from pathlib import Path

def main():

    # Create a Path Object:
    saved_games = Path("Saved Games")

    # Using home():
    print(Path.home()) # Output: C:\Users\nso89

    # Using joinpath():
    user_profile = Path.home()
    print(user_profile.joinpath(saved_games)) # Output: C:\Users\nso89\Saved Games

    # Using mkdirs():
    complete_path_to_saved_games = user_profile.joinpath(saved_games)
    complete_path_to_saved_games.mkdir(parents=True,exist_ok=True)

if __name__ == "__main__":
    main()
