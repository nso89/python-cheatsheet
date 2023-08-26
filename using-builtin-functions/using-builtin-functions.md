- [Using `filter()`](#using-`filter()`)
- [Using `map()`](#using-`map()`)
- [Using `sum()`](#using-`sum()`)
```python
def divide_by_two(number: int) -> bool:
    return number % 2 == 0


def multiply_by_two(number: int) -> int:
    return number * 2
    
zero_reminder : List[int] = [1,2,3,4,5,6,7,8,9,10]
```
#### <a name="using-`filter()`"></a>Using `filter()`:
```python
for number in filter(divide_by_two, zero_reminder):
    print(number)

# Output:
# 2
# 4 
# 6 
# 8 
# 10    
```
#### <a name="using-`map()`"></a>Using `map()`:
```python
for number in map(multiply_by_two, zero_reminder):
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
```
#### <a name="using-`sum()`"></a>Using `sum()`:
```python
numbers = [60, 9]
print(sum(numbers))

# Output:
# 69
```
