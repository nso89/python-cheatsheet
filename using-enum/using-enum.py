from enum import Enum


class CharacterType(Enum):
    ELF = 1
    KNIGHT = 2
    ORC = 3
    WIZARD = 4


def main():

    # Using Enum:
    print(CharacterType.ELF) # Output: CharacterType.ELF

    # Using name:
    print(CharacterType.ELF.name) # Output: ELF

    # Using value:
    print(CharacterType.ELF.value) # Output: 1

    # Using for:
    for character_type in CharacterType:
        print(character_type) 
    
    # Output: 
    # CharacterType.ELF
    # CharacterType.KNIGHT
    # CharacterType.ORC
    # CharacterType.WIZARD

if __name__ == "__main__":
    main()
