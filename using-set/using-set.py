from typing import Set


def main():

    # Using an empty set:
    empty = set()

    # Using set with elements:
    numbers : set = {1,2,3,4,5}
    print(numbers) # Output: {1, 2, 3, 4, 5}

    # Using add():
    numbers.add(69)
    print(numbers) # Output: {1, 2, 3, 4, 5, 69}

    # Using update():
    numbers.update([1,3,5,7,8,9,10])
    print(numbers) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}

    # Using intersection():
    print(numbers.intersection([1,3,5,7,8,9,10])) # Output: {1, 3, 5, 7, 8, 9, 10}
   
    # Using union():
    print(numbers.union([1,3,5,7,8,9,10])) # Output: {1, 2, 3, 4, 5, 69, 7, 8, 9, 10}

    # Using setdifference():
    print(numbers.difference([1,3,5,7,8,9,10])) # Output: {2, 4, 69}

if __name__ == "__main__":
    main()
