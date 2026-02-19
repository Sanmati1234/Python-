"""If/elif/else and truthiness examples."""


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main() -> None:
    print("Grade for 85:", grade(85))
    # ternary
    x = 5
    parity = "even" if x % 2 == 0 else "odd"
    print(x, parity)


if __name__ == "__main__":
    main()
