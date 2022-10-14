- [Creating an empty `tuple`](#create-an-empty-tuple)
- [Creating a `tuple` with elements](#creating-a-tuple-with-elements)
- [Unpacking a `tuple`](#unpacking-a-tuple)

#### <a name="create-an-empty-tuple"></a>Create an empty `tuple`:
```python
empty_tuple : tuple = ()
```
#### <a name="creating-a-tuple-with-elements"></a>Creating a `tuple` with elements`:
```python
svetlana  : tuple = ("Empress Svetlana",25,"Trance") # Output: ('Empress Svetlana', 25, 'Trance')
```
#### <a name="unpacking-a-tuple"></a>Unpacking a `tuple`:
```python
first_element, *middle, last_element = svetlana
print(f"{first_element}, {middle}, {last_element}") # Output: Empress Svetlana, [25], Trance
```
