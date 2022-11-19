- [Create an empty `Dict`](#create-an-empty-dict)
- [Create a `Dict` with items](#create-a-dict-with-items)
- [Using a `Dict` Comprehension](#using-a-dict-comprehension)
- [Adding an Item](#adding-an-item)
- [Using `get()`](#using-get())
- [Using `del`](#using-del)
- [Using `in`](#using-in)
- [Using `len()`](#using-len())
- [Using `pop()`](#using-pop())
- [Using `for`](#using-for)
- [Using `enumerate()`](#using-enumerate())
- [Using `clear()`](#using-clear())
#### <a name="create-an-empty-dict"></a> Create an empty `Dict`:
```python
empty_dict : Dict[str,int] = {}
```
#### <a name="create-a-dict-with-items"></a> Create a `Dict` with items:
```python
weapons : Dict[str,int] = {"Sword" : 20, "Axe": 10}
print(weapons) # Output: {'Sword': 20, 'Axe': 10}
```
#### <a name="using-a-dict-comprehension"></a> Using a `Dict` Comprehension:
```python
positions = {x[0]: x[1]  for x in [('A',69), ('B', 42), ('C', 17)]}
print(positions) # Output: {'A': 69, 'B': 42, 'C': 17} 
```
#### <a name="adding-an-item"></a> Adding an Item:
```python
weapons["Bow"] = 15
print(weapons) # Output: {'Sword': 20, 'Axe': 10, 'Bow': 15}
```
#### <a name="using-get()"></a> Using `get()`:
```python
damage = weapons.get("Sword")
print(damage) # Output: 20
```
#### <a name="using-del"></a> Using `del`:
```python
del weapons["Axe"]
print(weapons) # Output: {'Sword': 20, 'Bow': 15}
```
#### <a name="using-in"></a> Using `in`:
```python
if "Bow" in weapons:
    print("Bow in weapons.") # Output: Bow in weapons.
```
#### <a name="using-len()"></a> Using `len()`:
```python
print(len(weapons)) # Output: 2
```
#### <a name="using-pop()"></a> Using `pop()`:
```python
weapon = weapons.pop("Bow")
print(weapon) # Output: 15
```
#### <a name="using-for"></a> Using `for`:
```python
for key,value in weapons.items():
    print(f"Key: {key} Value: {value}") # Output: Key: Sword Value: 20
```
#### <a name="using-enumerate()"></a> Using `enumerate()`:
```python
for key,value in enumerate(weapons.items(), start = 1):
    print(f"Key: {key} Value: {value}") # Output: Key: 1 Value: ('Sword', 20)
```
#### <a name="using-clear()"></a> Using `clear()`:
```python
weapons.clear()
print(weapons) # Output: {}
```
