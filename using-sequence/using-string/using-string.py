def main():

    # Create a string:
    introduction : str = "hello world"
    
    # Print a string:
    print(introduction) # Output: hello world

    # Using title():
    print(introduction.title()) # Output: Hello World

    # Using strip():
    character_name = " Empress Svetlana "    
    print(character_name.strip()) # Output: Empress Svetlana

    # Using lower():
    character_name_lowered = character_name.lower()
    print(character_name_lowered) # Output: empress svetlana

    # Using replace():
    print(character_name_lowered.replace(" ","-")) # Output: empress-svetlana

    # Using f-string:
    print(f"{character_name.strip()}") # Output: Empress Svetlana

    # Using in:
    if "world" in introduction:
        print("String contains world.") # Output: String contains world.

    # Using startsswith()
    if introduction.startswith("he"):
        print("String starts with he.") # Output: String starts with he.

    # Using endswith():
    if introduction.endswith("orld"):
        print("String ends with orld.") # Output: Strng ends with orld.
    
    # Using split():
    print(introduction.split(" ")) # Output: ['hello', 'world']
    print(type(introduction.split(" ")))

    # Using len():
    print(len(introduction)) # Output: 11
     
if __name__ == "__main__":
    main()
