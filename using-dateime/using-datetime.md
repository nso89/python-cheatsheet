- [Using `filter()`](#using-filter())
- [Using `map()`](#using-map())
#### <a name="using-filter()"></a> Using `filter()`:
```python
zero_reminder : List[int] = [1,2,3,4,5,6,7,8,9,10]
for number in filter(divide_by_two,zero_reminder):
    print(number)

# Output:
# 2
# 4 
# 6 
# 8 
# 10
```
#### <a name="using-map()"></a> Using `map()`:
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
