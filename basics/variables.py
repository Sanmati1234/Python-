"""Variables examples for beginners."""

PI = 3.14159  # constant by convention


def examples() -> None:
    # simple assignments
    x = 10
    y = 2.5
    name = "Alice"

    # multiple assignment
    a, b, c = 1, 2, 3

    # mutable vs immutable
    nums = [1, 2, 3]
    nums.append(4)  # list is mutable

    # formatted string
    print(f"x={x}, y={y}, name={name}, PI={PI}")
    print("numbers:", nums)


if __name__ == "__main__":
    examples()
