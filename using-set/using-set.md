- [Create an empty `set`](#create-an-empty-set)
- [Create a `set` with elements](#create-a-set-with-elements)
- [Using `add()`](#using-add())
- [Using `update()`](#using-update())
- [Using `intersection()`](#using-intersection())
- [Using `union()`](#using-union())
- [Using `difference()`](#using-difference())

#### <a name="create-an-empty-set"></a>Create an empty `set`:
```python
empty_set = set()
```
#### <a name="create-a-set-with-elements"></a>Create a `set` with elements:
```python
numbers = set([1,2,3,4,5])
print(numbers) # Output: {1, 2, 3, 4, 5}
```
#### <a name="using-add()"></a>Using `add()`:
```python
numbers.add(69)
print(numbers) # Output: {1, 2, 3, 4, 5, 69}
```
#### <a name="using-update()"></a>Using `update()`:
```python
numbers.update([1,3,5,7,8,9,10])
print(numbers) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}
```
#### <a name="using-intersection()"></a>Using `intersection()`:
```python
print(numbers.intersection([1,3,5,7,8,9,10])) # Output: {1, 3, 5, 7, 8, 9, 10}
```
#### <a name="using-union()"></a>Using `union()`:
```python
print(numbers.union([1,3,5,7,8,9,10])) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}
```
#### <a name="using-difference()"></a>Using `difference()`:
```python
print(numbers.difference([1,3,5,7,8,9,10])) # Output: {2, 4, 69}
```
