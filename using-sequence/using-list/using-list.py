from typing import List


def main():

    # Using an empty List:
    empty_list : List[str] = []

    # Using List with elements:
    friends : List[str] = ["Scott","Annabelle","Dasha","Charles"]
    print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Charles']

    # Using List comprehension:
    names_with_e = [name for name in friends if "e" in name ]
    print(names_with_e) # Output: ['Annabelle', 'Charles']

    # Using append():
    friends.append("Svetlana")
    print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Charles', 'Svetlana']

    # Using index:
    print(friends[2]) # Output: Dasha

    # Using remove():
    friends.remove("Charles")
    print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Svetlana']

    # Using in:
    if "Dasha" in friends:
        print("Dasha is in the friends list.") # Output: Dasha is in the friends list.

    # Using len():
    print(len(friends)) # Output: 4

    # Using sort():
    friends.sort()
    print(friends) # Output: ['Annabelle', 'Dasha', 'Scott', 'Svetlana']

    # Using join():
    acquaintances : str = " ".join(friends)
    print(acquaintances) # Output: Annabelle Dasha Scott Svetlana 

    # Using pop():
    last_friend = friends.pop()
    print(last_friend) # Output: Svetlana

    # Using for:
    for friend in friends:
        print(friend) # Output: Scott, Annabelle, Dasha, Svetlana

    # Using enumerate():
    for index, friend in enumerate(friends, start = 1):
        print(f"{index}.{friend}") # Output: 1.Scott 2.Annabelle 3.Dasha 4.Svetlana

    # Using clear():
    friends.clear()
    print(friends) # Output: []

if __name__ == "__main__":
    main()
