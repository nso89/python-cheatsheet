from typing import List


def write_a_str_to_a_file(file_name: str, word: str) -> None:
    with open(file_name, "w") as stream:
        stream.write(f"{word}\n")


def read_a_str_from_a_file(file_name: str) -> str:
    line : str = ""
    with open(file_name, "r") as stream:
        line = stream.readline()
    return line


def append_a_str_to_a_file(file_name: str, word: str) -> None:
    with open(file_name, "a") as stream:
        stream.write(f"{word}\n")


def write_a_list_to_a_file(file_name: str, items: List[str]) -> List[str]:
    with open(file_name, "w") as stream:
        for word in items:
            stream.write(f"{word}\n")


def read_a_list_from_a_file(file_name: str) -> List[str]: 
    with open(file_name) as f_obj:
        lines = f_obj.readlines()
    return lines


def main():
    
    friends : str = "friends.txt"
    team_members : str = "team_members.txt"
    file_name : str = "introduction.txt"
    
    # Write a str to a file:
    write_a_str_to_a_file(file_name = friends, word = "Charles")
    
    # Reading a str from a file:
    introduction : str  = read_a_str_from_a_file(file_name = file_name)
    print(introduction)

    # Appending a str to a file:
    append_a_str_to_a_file(file_name = friends, word = "Olivia")
    
    # Writing a List to a file:
    team_mates : List[str] = ["Scott", "Annabelle", "Dasha", "Svetlana"] 
    write_a_list_to_a_file(file_name = team_members, items = team_mates)
    
    # Reading a List from a file:
    print(read_a_list_from_a_file(file_name = team_members))
     
if __name__ == "__main__":
    main()
