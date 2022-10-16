from pathlib import Path

def main():

    # Create a Path Object:
    saved_3D_games = Path("Saved 3D Games")

    # Using home():
    print(Path.home()) # Output: C:\Users\nso89

    # Using joinpath():
    user_profile = Path.home()
    print(user_profile.joinpath(saved_3D_games)) # Output: C:\Users\nso89\Saved 3D Games

    # Using mkdirs():
    complete_path_to_saved_3d_games = user_profile.joinpath(saved_games)
    complete_path_to_saved_3d_games.mkdir(parents=True,exist_ok=True)

    # Using rmdir():
    complete_path_to_saved_3d_games.rmdir()

if __name__ == "__main__":
    main()
