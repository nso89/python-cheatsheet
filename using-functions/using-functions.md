- [Using `pass`](#using-pass)
- [Using a function with parameters](#using-a-function-with-parameters)
- [Using `return`](#using-return)
- [Using positional arguments](#using-positional-arguments)
- [Using keyword arguments](#using-keyword-arguments)
#### <a name="using-pass"></a>Using `pass`:
```python
def empty_function() -> None:
    pass
```
#### <a name="using-a-function-with-parameters"></a>Using a function with parameters:
```python
def add(collection: List[str], item: str) -> None:
    collection.append(item)

inventory : List[str] = ["Book", "Compass", "Potion"]
add(collection = inventory, item = "Orb of Truth")
print(inventory) # Output: ['Book', 'Compass', 'Potion', 'Orb of Truth']
```
#### <a name="using-return"></a> Using `return`:
```python
def get_mana_level() -> int:
    return 69

print(get_mana_level()) # Output: 69
```
#### <a name="using-positional-arguments"></a>Using positional arguments:
```python
def team_members(*members):
    print(f"List of Team Members:")
    for index, member in enumerate(members, start=1):
        print(f"{index}.{member}")

team_members('Scott', 'Annabelle', 'Dasha', 'Charles', 'Svetlana')

# Output:
# List of Team Members:
# 1. Scott
# 2. Annabelle
# 3. Dasha
# 4. Charles
# 5. Svetlana
```
#### <a name="using-keyword-arguments"></a>Using keyword arguments:
```python
def character_attributes(**attribs):
    print("Character Attributes:")
    for keyword,value in attribs.items():
        print(f"{keyword}: {value}")

character_attributes(name = "Empress Svetlana", age = 22, music_genre = "Trance", drink = "Mint Hot Chocolate")

# Output:
# Character Attributes:
# name: Empress Svetlana
# age: 22
# music_genre: Trance
# drink: Mint Hot Chocolate
```
