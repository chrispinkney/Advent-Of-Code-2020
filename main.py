import day_one
import day_two
import time


def main():
    start = time.time()

    # day_one.d1()
    day_two.d2()

    end = time.time()
    print(f"Total Time to Run: {end - start} seconds.")


if __name__ == "__main__":
    main()
