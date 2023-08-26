from typing import List


def divide_by_two(number: int) -> bool:
    return number % 2 == 0


def multiply_by_two(number: int) -> int:
    return number * 2


def main():
    
    # Using filder():
    zero_reminder : List[int] = [1,2,3,4,5,6,7,8,9,10]
    for number in filter(divide_by_two, zero_reminder):
        print(number)
        
    # Output:
    # 2
    # 4 
    # 6 
    # 8 
    # 10
    
    # Using map():
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

    # Using sum():
    numbers = [60, 9]
    print(sum(numbers))

    # Output:
    # 69
    
if __name__ == "__main__":
    main()
