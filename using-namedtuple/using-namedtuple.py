from typing import NamedTuple


# Using NamedTuple:
class Weapon(NamedTuple):
    name:str
    damage:int

    def __str__(self) -> str:
        return f"Name: {self.name} Damage: {self.damage}"


def main():
    
    # Getting a field value:
    sword = Weapon(name = "Sword", damage = 10)
    print(sword.damage) # Output: 10

    # Using __str__():
    print(sword) # Output: Name: Sword Damage: 10

if __name__ == "__main__":
    main()
