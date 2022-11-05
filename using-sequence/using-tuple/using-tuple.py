def main():

    # Creating an empty tuple:
    empty_tuple : tuple = ()

    # Creating a tuple with elements:
    svetlana  : tuple = ("Empress Svetlana",25,"Trance")
    print(svetlana) # Output: ('Empress Svetlana', 25, 'Trance')

    # Unpacking a tuple:
    first_element, *middle, last_element = svetlana
    print(f"{first_element}, {middle}, {last_element}") # Output: Empress Svetlana, [25], Trance

if __name__ == "__main__":
    main()
