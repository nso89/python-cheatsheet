- [Using an empty `Dict`](#using-an-empty-dict)
- [Using `Dict` with elements](#using-dict-with-elements)
- [Using `Dict` Comprehension](#using-dict-comprehension)
- [Adding an element](#adding-an-element)
- [Using `get()`](#using-get())
- [Using `del`](#using-del)
- [Using `in`](#using-in)
- [Using `len()`](#using-len())
- [Using `sorted()`](#using-sorted())
- [Using `pop()`](#using-pop())
- [Using `for`](#using-for)
- [Using `enumerate()`](#using-enumerate())
- [Using `clear()`](#using-clear())
#### <a name="using-an-empty-dict"></a>Using an empty `Dict`:
```python
empty_dict : Dict[str,int] = {}
```
#### <a name="using-dict-with-elements"></a>Using `Dict` with elements:
```python
weapons : Dict[str,int] = {"Sword" : 20, "Axe": 10}
print(weapons) # Output: {'Sword': 20, 'Axe': 10}
```
#### <a name="using-dict-comprehension"></a>Using `Dict` Comprehension:
```python
positions = {letter:number for letter, number in [('A',69), ('B', 42), ('C', 17)]}
print(positions) # Output: {'A': 69, 'B': 42, 'C': 17} 
```
#### <a name="adding-an-element"></a>Adding an Item:
```python
weapons["Bow"] = 15
print(weapons) # Output: {'Sword': 20, 'Axe': 10, 'Bow': 15}
```
#### <a name="using-get()"></a>Using `get()`:
```python
damage = weapons.get("Sword")
print(damage) # Output: 20
```
#### <a name="using-del"></a>Using `del`:
```python
del weapons["Axe"]
print(weapons) # Output: {'Sword': 20, 'Bow': 15}
```
#### <a name="using-in"></a>Using `in`:
```python
if "Bow" in weapons:
    print("Bow in weapons.") # Output: Bow in weapons.
```
#### <a name="using-len()"></a>Using `len()`:
```python
print(len(weapons)) # Output: 2
```
#### <a name="using-sorted()"></a>Using `sorted()`:
```python
print(dict(sorted(weapons.items()))) # Output: {'Bow': 15, 'Sword': 20}
```
#### <a name="using-pop()"></a>Using `pop()`:
```python
weapon = weapons.pop("Bow")
print(weapon) # Output: 15
```
#### <a name="using-for"></a>Using `for`:
```python
for key, value in weapons.items():
    print(f"Key: {key} Value: {value}") # Output: Key: Sword Value: 20
```
#### <a name="using-enumerate()"></a>Using `enumerate()`:
```python
for key, value in enumerate(weapons.items(), start = 1):
    print(f"Key: {key} Value: {value}") # Output: Key: 1 Value: ('Sword', 20)
```
#### <a name="using-clear()"></a>Using `clear()`:
```python
weapons.clear()
print(weapons) # Output: {}
```
