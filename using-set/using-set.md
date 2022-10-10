- [Create an empty `set`](#create-an-empty-set)
- [Create a `set` with elements](#create-a-set-with-elements)
- [Using `intersection()`](#using-intersection())
- [Using `union()`](#using-union())
- [Using `difference()`](#using-difference())

#### <a name="create-an-empty-set"></a>Create an empty `set`:
```python
empty_set = set()
```
#### <a name="create-a-set-with-elements"></a>Create a `set` with elements:
```python
numbers = set([21,57,17,41,42,60,83,69,87]) # Output: {69, 41, 42, 17, 83, 21, 87, 57, 60}
```
#### <a name="using-intersection()"></a>Using `intersection()`:
```python
other_numbers = set([70,34,69,44,25,17])
print(numbers.intersection(other_numbers)) # Output: {17, 69}
```
#### <a name="using-union()"></a>Using `union()`:
```python
print(numbers.union(other_numbers)) # Output: {34, 69, 70, 41, 42, 44, 17, 83, 21, 87, 57, 60, 25}
```
#### <a name="using-difference()"></a>Using `difference()`:
```python
print(numbers.difference(other_numbers)) # Output: {41, 42, 83, 21, 87, 57, 60}
```
