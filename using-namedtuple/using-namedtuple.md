- [Using `NamedTuple`](#using-namedtuple)
- [Getting a field value](#getting-a-field-value)
- [Using `__str__()`](#using-__str__())
#### <a name="using-namedtuple"></a>Using `NamedTuple`:
```python
class Weapon(NamedTuple):
    name:str
    damage:int

    def __str__(self) -> str:
        return f"Name: {self.name} Damage: {self.damage}"
```
#### <a name="getting-a-field-value"></a>Getting a field value:
```python
sword = Weapon(name = "Sword", damage = 10)
print(sword.damage) # Output: 10
```
#### <a name="using-__str__()"></a>Using `__str__()`:
```python
print(sword) # Output: Name: Sword Damage: 10
```
