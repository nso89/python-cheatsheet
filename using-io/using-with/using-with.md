- [Write a string to a file](#write-a-string-to-a-file)
- [Appending a string to a file](#appending-a-string-to-a-file)
- [Writing a `List` to a file](#writing-a-list-to-a-file)
- [Reading a `List` from a file](#reading-a-list-from-a-file)
#### <a name="write-a-string-to-a-file"></a> Write a string to a file:
```python
friends = "friends.txt"
team_members = "team_members.txt"
    
write_a_string_to_a_file(file_name=friends,word="Charles")
```
#### <a name="appending-a-string-to-a-file"></a> Appending a string to a file:
```python
append_a_string_to_a_file(file_name=friends,word="Olivia")
```
#### <a name="writing-a-list-to-a-file"></a> Writing a `List` to a file:
```python
team_mates : List[str] = ["Scott","Annabelle","Dasha","Svetlana"] 
write_a_list_to_a_file(file_name=team_members,items=team_mates)
```
#### <a name="reading-a-list-from-a-file"></a> Reading a `List` from a file:
```python
print(read_a_list_from_a_file(file_name=team_members))
```
