from typing import Dict


def main():

    # Using an empty Dict:
    empty_dict : Dict[str,int] = {}

    # Using Dict with elements:
    weapons : Dict[str,int] = {"Sword" : 20, "Axe": 10}
    print(weapons) # Output: {'Sword': 20, 'Axe': 10}

    # Using Dict Comprehension:
    positions = {letter:number for letter, number in [('A',69), ('B', 42), ('C', 17)]}
    print(positions) # Output: {'A': 69, 'B': 42, 'C': 17}

    # Adding an element:
    weapons["Bow"] = 15
    print(weapons) # Output: {'Sword': 20, 'Axe': 10, 'Bow': 15}

    # Using get():
    damage = weapons.get("Sword")
    print(damage) # Output: 20

    # Using del:
    del weapons["Axe"]
    print(weapons) # Output: {'Sword': 20, 'Bow': 15}

    # Using in:
    if "Bow" in weapons:
        print("Bow in weapons.") # Output: Bow in weapons.
    
    # Using len():
    print(len(weapons)) # Output: 2

    # Using sorted():
    print(dict(sorted(weapons.items()))) # Output: {'Bow': 15, 'Sword': 20}

    # Using pop():
    weapon = weapons.pop("Bow")
    print(weapon) # Output: 15

    # Using for:
    for key, value in weapons.items():
        print(f"Key: {key} Value: {value}") # Output: Key: Sword Value: 20

    # Using enumerate():
    for key, value in enumerate(weapons.items(), start = 1):
        print(f"Key: {key} Value: {value}") # Output: Key: 1 Value: ('Sword', 20)
    
    # Using clear():
    weapons.clear()
    print(weapons) # Output: {}

if __name__ == "__main__":
    main()
