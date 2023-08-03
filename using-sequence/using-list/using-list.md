- [Using an empty `List`](#using-an-empty-list)
- [Using `List` with elements](#using-list-with-elements)
- [Using `List` comprehension](#using-list-comprehension)
- [Using `append()`](#using-append())
- [Using `index`](#using-index)
- [Using `remove()`](#using-remove())
- [Using `in`](#using-in)
- [Using `len()`](#using-len())
- [Using `sort()`](#using-sort())
- [Using `join()`](#using-join())
- [Using `pop()`](#using-pop())
- [Using `for`](#using-for)
- [Using `enumerate()`](#using-enumerate())
- [Using `clear()`](#using-clear())
#### <a name="using-an-empty-list"></a>Using an empty `List`:
```python
empty_list : List[str] = []
```
#### <a name="using-list-with-elements"></a>Using `List` with elements:
```python
friends : List[str] = ["Scott","Annabelle","Dasha","Charles"]
print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Charles']
```
#### <a name="using-list-comprehension"></a>Using `List` comprehension:
```python
names_with_e = [name for name in friends if "e" in name ]
print(names_with_e) # Output: ['Annabelle', 'Charles']
```
#### <a name="using-append()"></a>Using `append()`:
```python
friends.append("Svetlana")
print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Charles', 'Svetlana']
```
#### <a name="using-index"></a>Using `index`:
```python
print(friends[2]) # Output: Dasha
```
#### <a name="using-remove()"></a>Using `remove()`:
```python
friends.remove("Charles")
print(friends) # Output: ['Scott', 'Annabelle', 'Dasha', 'Svetlana']
```
#### <a name="using-in"></a>Using `in`:
```python
if "Dasha" in friends:
    print("Dasha is in the friends list.") # Output: Dasha is in the friends list.
```
#### <a name="using-len()"></a>Using `len()`:
```python
print(len(friends)) # Output: 4
```
#### <a name="using-sort()"></a>Using `sort()`:
```python
friends.sort()
print(friends) # Output: ['Annabelle', 'Dasha', 'Scott', 'Svetlana']
```
#### <a name="using-join()"></a>Using `join()`:
```python
friends_str : str = " ".join(friends)
print(friends_str) # Output: Annabelle Dasha Scott Svetlana 
```
#### <a name="using-pop()"></a>Using `pop()`:
```python
last_friend = friends.pop()
print(last_friend) # Output: Svetlana
```
#### <a name="using-for"></a>Using `for`:
```python
for friend in friends:
    print(friend) # Output: Scott, Annabelle, Dasha, Svetlana
```
#### <a name="using-enumerate()"></a>Using `enumerate()`:
```python
for index, friend in enumerate(friends, start = 1):
    print(f"{index}.{friend}") # Output: 1.Scott 2.Annabelle 3.Dasha 4.Svetlana
```
#### <a name="using-clear()"></a>Using `clear()`:
```python
friends.clear()
print(friends) # Output: []
```
