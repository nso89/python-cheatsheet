- [Using an empty `tuple`](#using-an-empty-tuple)
- [Using a `tuple` with elements](#using-a-tuple-with-elements)
- [Unpacking a `tuple`](#unpacking-a-tuple)
#### <a name="using-an-empty-tuple"></a>Using an empty `tuple`:
```python
empty_tuple : tuple = ()
```
#### <a name="using-a-tuple-with-elements"></a>Using a `tuple` with elements:
```python
svetlana  : tuple = ("Empress Svetlana",25,"Trance")
print(svetlana) # Output: ('Empress Svetlana', 25, 'Trance')
```
#### <a name="unpacking-a-tuple"></a>Unpacking a `tuple`:
```python
first_element, *middle, last_element = svetlana
print(f"{first_element}, {middle}, {last_element}") # Output: Empress Svetlana, [25], Trance
```
