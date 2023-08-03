- [Using `str`](#using-str)
- [Using `str` with `print()`](#print-a-str)
- [Using `title()`](#using-title())
- [Using `strip()`](#using-strip())
- [Using `lower()`](#using-lower())
- [Using `replace()`](#using-replace())
- [Using `f-string`](#using-f-string)
- [Using `in`](#using-in)
- [Using `startswith()`](#using-startswith())
- [Using `endswith()`](#using-endswith())
- [Using `split()`](#using-split())
- [Using `len()`](#using-len())
#### <a name="using-str"></a>Using `str`:
```python
introduction : str = "hello world"
```
#### <a name="using-str-with-print()"></a>Using `str` with `print()`:
```python
print(introduction) # Output: hello world
```
#### <a name="using-title()"></a>Using `title()`:
```python
print(introduction.title()) # Output: Hello World
```
#### <a name="using-strip()"></a>Using `strip()`:
```python
character_name = " Empress Svetlana "    
print(character_name.strip()) # Output: Empress Svetlana
```
#### <a name="using-lower()"></a>Using `lower()`:
```python
character_name_lowered = character_name.lower()
print(character_name_lowered) # Output: empress svetlana
```
#### <a name="using-replace()"></a>Using `replace()`:
```python
print(character_name_lowered.replace(" ","-")) # Output: empress-svetlana
```
#### <a name="using-f-string"></a>Using `f-string`:
```python
print(f"{character_name.strip()}") # Output: Empress Svetlana
```
#### <a name="using-in"></a>Using `in`:
```python
if "world" in introduction:
    print("String contains world.") # Output: String contains world.
```
#### <a name="using-startswith()"></a>Using `startswith()`:
```python
if introduction.startswith("he"):
    print("String starts with he.") # Output: String starts with he.
```
#### <a name="using-endswith()"></a>Using `endswith()`:
```python
if introduction.endswith("orld"):
    print("String ends with orld.") # Output: Strng ends with orld.
```
#### <a name="using-split()"></a>Using `split()`:
```python
print(introduction.split(" ")) # Output: ['hello', 'world']
print(type(introduction.split(" "))) # Output: <class 'list'>
```
#### <a name="using-len()"></a>Using `len()`:
```python
print(len(introduction)) # Output: 11
```
