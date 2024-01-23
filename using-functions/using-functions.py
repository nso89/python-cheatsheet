from typing import List


def empty_function() -> None:
    pass


def add(collection: List[str], item: str) -> None:
    collection.append(item)


def get_mana_level() -> int:
    return 69


def team_members(*members):
    print(f"List of Team Members:")
    for index, member in enumerate(members, start = 1):
        print(f"{index}.{member}")


def character_attributes(**attribs):
    print("Character Attributes:")
    for keyword,value in attribs.items():
        print(f"{keyword}: {value}")


def main():

    # Using pass:
    empty_function()

    # Using a function with parameters:
    inventory : List[str] = ["Book", "Compass", "Potion"]
    add(collection = inventory, item = "Orb of Truth")
    print(inventory) # Output: ['Book', 'Compass', 'Potion', 'Orb of Truth']

    # Using return:
    print(get_mana_level()) # Output: 69

    # Using positional arguments:
    team_members('Scott', 'Annabelle', 'Dasha', 'Charles', 'Svetlana')

    # Output:
    # List of Team Members:
    # 1. Scott
    # 2. Annabelle
    # 3. Dasha
    # 4. Charles
    # 5. Svetlana

    # Using keyword arguments:
    character_attributes(name = "Empress Svetlana", age = 22, music_genre = "Trance", drink = "Mint Hot Chocolate")

    # Output:
    # Character Attributes:
    # name: Empress Svetlana
    # age: 22
    # music_genre: Trance
    # drink: Mint Hot Chocolate

if __name__ == "__main__":
    main()
