"""Simple command-line calculator.

Supports add, sub, mul, div with two operands.
"""


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def main() -> None:
    print("Simple Calculator")
    print("Enter expressions like: 2 + 3")
    while True:
        try:
            line = input("calc> ").strip()
            if not line:
                continue
            if line.lower() in ("q", "quit", "exit"):
                print("Goodbye")
                break

            parts = line.split()
            if len(parts) != 3:
                print("Enter: <num> <op> <num> (e.g. 2 * 5)")
                continue

            a_s, op, b_s = parts
            a = float(a_s)
            b = float(b_s)
            if op not in OPS:
                print("Unsupported operator. Use + - * /")
                continue

            result = OPS[op](a, b)
            print(result)

        except ValueError:
            print("Invalid number format. Try again.")
        except ZeroDivisionError as e:
            print(e)


if __name__ == "__main__":
    main()
