from typing import Set

def main():

    # Creating an empty set:
    empty_set = set()

    # Creating a set with elements:
    numbers = set([21,57,17,41,42,60,83,69,87])
    print(numbers) # Output: {69, 41, 42, 17, 83, 21, 87, 57, 60}

    # Using intersection():
    other_numbers = set([70,34,69,44,25,17])
    print(numbers.intersection(other_numbers)) # Output: {17, 69}

    # Using union():
    print(numbers.union(other_numbers)) # Output: {34, 69, 70, 41, 42, 44, 17, 83, 21, 87, 57, 60, 25}

    # Using setdifference():
    print(numbers.difference(other_numbers)) # Output: {41, 42, 83, 21, 87, 57, 60}

if __name__ == "__main__":
    main()
