- [Using `Path()`](#using-path)
- [Using `home()`](#using-home())
- [Using `joinpath()`](#using-joinpath())
- [Using `mkdir()`](#using-mkdir())
- [Using `parent()`](#using-parent())
- [Using `iterdir()`](#using-iterdir())
- [Using `is_dir()`](#using-is_dir())
- [Using `is_file()`](#using-is_file())
- [Using `stem`](#using-stem)
- [Using `name`](#using-name)
- [Using `suffix`](#using-suffix)
- [Using `rmdir()`](#using-rmdir())
- [Using `with_suffix()`](#using-with_suffix())
#### <a name="using-path"></a> Using `Path()`:
```python
saved_3D_games = Path("Saved 3D Games")
```
#### <a name="using-home()"></a> Using `home()`:
```python
print(Path.home()) # Output: C:\Users\nso89
```
#### <a name="using-joinpath()"></a> Using `joinpath()`:
```python
user_profile = Path.home()
print(user_profile.joinpath(saved_3D_games)) # Output: C:\Users\nso89\Saved 3D Games
```
#### <a name="using-mkdir()"></a> Using `mkdir()`:
```python
complete_path_to_saved_3d_games = user_profile.joinpath(saved_3D_games)
complete_path_to_saved_3d_games.mkdir(parents = True, exist_ok = True)
```
#### <a name="using-parent()"></a> Using `parent()`:
```python
print(complete_path_to_saved_3d_games.parent) # Output: C:\Users\nso89
```
#### <a name="using-iterdir()"></a> Using `iterdir()`:
```python
documents = Path.home().joinpath("Documents").joinpath("Work")
for file in documents.iterdir():
    print(file)

# Output:
# C:\Users\nso89\Documents\Work\companies.txt
# C:\Users\nso89\Documents\Work\cover-letter-resume.odt
# C:\Users\nso89\Documents\Work\Deep Space Nine
# C:\Users\nso89\Documents\Work\Enterprise 
```
#### <a name="using-is_dir()"></a> Using `is_dir()`:
```python
for file in documents.iterdir():
    if file.is_dir():
        print(file)

# Output:
# C:\Users\nso89\Documents\Work\Deep Space Nine
# C:\Users\nso89\Documents\Work\Enterprise
```
#### <a name="using-is_file()"></a> Using `is_file()`:
```python
for file in documents.iterdir():
    if file.is_file():
        print(file)

# Output:
# C:\Users\nso89\Documents\Work\companies.txt
# C:\Users\nso89\Documents\Work\cover-letter-resume.odt
```
#### <a name="using-stem"></a> Using `stem`:
```python
game_save_file = complete_path_to_saved_3d_games.joinpath("progress.gsv")
print(game_save_file.stem) # Output: progress
```
#### <a name="using-name"></a> Using `name`:
```python
print(game_save_file.name) # Output: progress.gsv
```
#### <a name="using-suffix"></a> Using `suffix`:
```python
print(game_save_file.suffix) # Output: .gsv
```
#### <a name="using-rmdir()"></a> Using `rmdir()`:
```python
complete_path_to_saved_3d_games.rmdir()
```
#### <a name="using-with_suffix()"></a> Using `with_suffix()`:
```python
print(game_save_file.with_suffix(".gs")) # Output: progress.gs
```
