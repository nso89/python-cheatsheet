- [Using comments](#using-comments)
- [Using docstring](#using-docstring)
#### <a name="using-comments"></a> Using comments:
```python
# This is a comment.
```
#### <a name="using-docstring"></a> Using docstring:
```python
def convert_comment_to_markdown_syntax(keywords : set[str], verify : str) -> str:
    """
    Check a string against a set of keywords, if the string exists, add 
    backquotes, and append it to the list. If the word doesn't exist, just 
    append to the list.
    
    Args:
        keywords : set[str] - the set containing our keywords.
        verify : str - the word were checking for in our set.
    
    Returns:
        Using .join(), we return our string properly quoted.
        
    Example:
        Using title() becomes Using `title()`
    """
    return " ".join([f"`{word}`" if word in keywords else word for word in verify.split(" ")])
```
