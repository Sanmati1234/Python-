"""Demonstrate common Python data types and simple operations."""


def demo() -> None:
    # Numbers
    i = 7
    f = 3.14

    # Strings
    s = "hello"
    s2 = "world"

    # Collections
    lst = [1, 2, 3]
    tpl = (1, 2, 3)
    d = {"a": 1, "b": 2}
    st = {1, 2, 3}

    print(i, f, s + " " + s2)
    print("list slice:", lst[1:])
    print("tuple unpack:", *tpl)
    print("dict keys:", list(d.keys()))
    print("set contains 2?", 2 in st)

    # conversions
    print("int->str:", str(i))
    print("str->int:", int("10"))


if __name__ == "__main__":
    demo()
