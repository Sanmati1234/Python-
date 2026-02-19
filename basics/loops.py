"""Loop examples: for, while, enumerate, comprehensions."""


def iterate_list(items: list[int]) -> None:
    for i, v in enumerate(items):
        print(i, v)


def while_count(n: int) -> None:
    i = 0
    while i < n:
        if i % 2 == 0:
            print(i, "even")
        i += 1


def comprehensions() -> None:
    evens = [x for x in range(10) if x % 2 == 0]
    squares = {x: x * x for x in range(6)}
    print("evens", evens)
    print("squares", squares)


if __name__ == "__main__":
    iterate_list([10, 20, 30])
    while_count(5)
    comprehensions()
