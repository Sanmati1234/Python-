"""Function definitions, args, kwargs, and higher-order functions."""


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def sum_all(*nums: int) -> int:
    return sum(nums)


def apply_operation(a: int, b: int, op) -> int:
    return op(a, b)


def main() -> None:
    print(greet("Sam"))
    print("sum:", sum_all(1, 2, 3, 4))
    print("mul via lambda:", apply_operation(3, 4, lambda x, y: x * y))


if __name__ == "__main__":
    main()
