- [Creating an empty `set`](#creating-an-empty-set)
- [Creating a `set` with elements](#creating-a-set-with-elements)
- [Using `add()`](#using-add())
- [Using `update()`](#using-update())
- [Using `intersection()`](#using-intersection())
- [Using `union()`](#using-union())
- [Using `setdifference()`](#using-setdifference())
#### <a name="creating-an-empty-set"></a> Creating an empty `set`:
```python
empty_set = set()
```
#### <a name="creating-a-set-with-elements"></a> Creating a `set` with elements:
```python
numbers = set([1,2,3,4,5])
print(numbers) # Output: {1, 2, 3, 4, 5}
```
#### <a name="using-add()"></a> Using `add()`:
```python
numbers.add(69)
print(numbers) # Output: {1, 2, 3, 4, 5, 69}
```
#### <a name="using-update()"></a> Using `update()`:
```python
numbers.update([1,3,5,7,8,9,10])
print(numbers) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}
```
#### <a name="using-intersection()"></a> Using `intersection()`:
```python
print(numbers.intersection([1,3,5,7,8,9,10])) # Output: {1, 3, 5, 7, 8, 9, 10}
```
#### <a name="using-union()"></a> Using `union()`:
```python
print(numbers.union([1,3,5,7,8,9,10])) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}
```
#### <a name="using-setdifference()"></a> Using `setdifference()`:
```python
print(numbers.difference([1,3,5,7,8,9,10])) # Output: {2, 4, 69}
```
