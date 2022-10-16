- [Create a `Path` Object](#create-a-path-object)
- [Using `home()`](#using-home())
- [Using `joinpath()`](#using-joinpath())
- [Using `mkdirs()`](#using-mkdirs())

#### <a name="create-a-path-object"></a> Create a `Path` Object:
```python
saved_games = Path("Saved Games")
```
#### <a name="using-home()"></a> Using `home()`:
```python
print(Path.home()) # Output: C:\Users\nso89
```
#### <a name="using-joinpath()"></a> Using `joinpath`():
```python
user_profile = Path.home()
print(user_profile.joinpath(saved_games)) # Output: C:\Users\nso89\Saved Games
```
#### <a name="using-mkdirs()"></a> Using `mkdirs()`: 
```python
complete_path_to_saved_games = user_profile.joinpath(saved_games)
complete_path_to_saved_games.mkdir(parents=True,exist_ok=True)
```
