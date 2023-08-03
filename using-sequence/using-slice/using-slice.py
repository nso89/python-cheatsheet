from typing import Sequence


def main():

    friends : Sequence = "Annabelle and Svetlana"

    # Slicing Out the First x Elements:
    print(friends[4:]) # Output: belle and Svetlana

    # Slicing Out the Last x Elements: 
    print(friends[:-4]) # Output: Annabelle and Svet

    # Slicing the First x Elements:
    print(friends[:4]) # Output: Anna

    # Slicing the Last x Elements:
    print(friends[-4:]) # Output: lana

if __name__ == "__main__":
    main()
