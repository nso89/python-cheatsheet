from pathlib import Path


def main():

    # Using Path():
    saved_3D_games = Path("Saved 3D Games")

    # Using home():
    print(Path.home()) # Output: C:\Users\nso8

    # Using joinpath():
    user_profile = Path.home()
    print(user_profile.joinpath(saved_3D_games)) # Output: C:\Users\nso89\Saved 3D Games

    # Using mkdir():
    complete_path_to_saved_3d_games = user_profile.joinpath(saved_3D_games)
    complete_path_to_saved_3d_games.mkdir(parents = True, exist_ok = True)

    # Using parent():
    print(complete_path_to_saved_3d_games.parent) # Output: C:\Users\nso89

    # Using iterdir():
    documents = Path.home().joinpath("Documents").joinpath("Work")
    for file in documents.iterdir():
        print(file)
    
    # Output:
    # C:\Users\nso89\Documents\Work\companies.txt
    # C:\Users\nso89\Documents\Work\cover-letter-resume.odt
    # C:\Users\nso89\Documents\Work\Deep Space Nine
    # C:\Users\nso89\Documents\Work\Enterprise

    # Using is_dir():
    for file in documents.iterdir():
        if file.is_dir():
            print(file)
    
    # Output:
    # C:\Users\nso89\Documents\Work\Deep Space Nine
    # C:\Users\nso89\Documents\Work\Enterprise

    # Using is_file():
    for file in documents.iterdir():
        if file.is_file():
            print(file)
    
    # Output:
    # C:\Users\nso89\Documents\Work\companies.txt
    # C:\Users\nso89\Documents\Work\cover-letter-resume.odt
    
    # Using stem:
    game_save_file = complete_path_to_saved_3d_games.joinpath("progress.gsv")
    print(game_save_file.stem) # Output: progress

    # Using name:
    print(game_save_file.name) # Output: progress.gsv

    # Using suffix:
    print(game_save_file.suffix) # Output: .gsv

    # Using rmdir():
    complete_path_to_saved_3d_games.rmdir()

    # Using with_suffix():
    print(game_save_file.with_suffix(".gs")) # Output: progress.gs

if __name__ == "__main__":
    main()
