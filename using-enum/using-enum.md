- [Using an `Enum`](#using-an-enum)
- [Using `name`](#using-name)
- [Using `value`](#using-value)
- [Using `for`](#using-for)
#### <a name="using-an-enum"></a> Using an `Enum`:
```python
print(CharacterType.ELF) # Output: CharacterType.ELF
```
#### <a name="using-name"></a> Using `name`:
```python
print(CharacterType.ELF.name) # Output: ELF
```
#### <a name="using-value"></a> Using `value`:
```python
print(CharacterType.ELF.value) # Output: 1
```
#### <a name="using-for"></a> Using `for`:
```python
for character_type in CharacterType:
    print(character_type) 

# Output: 
# CharacterType.ELF
# CharacterType.KNIGHT
# CharacterType.ORC
# CharacterType.WIZARD
```
