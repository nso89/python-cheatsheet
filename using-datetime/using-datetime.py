from datetime import datetime
import time


def main():

    # Using datetime.now() with strftime():
    print(datetime.now().strftime("%Y%m%d-%H%M%S"))

    # Using time.strftime():
    print(time.strftime("%Y%m%d-%H%M%S"))

if __name__ == "__main__":
    main()
