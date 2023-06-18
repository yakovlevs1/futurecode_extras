from main import solve_square_eq


def show_result(result: list[float]) -> None:
    if len(result) == 0:
        print("У заданного уравнения нет решений")
    elif len(result) == 1:
        print(f"У уравнения один кратный корень, равный {result[0]:0.3f}")
    else:
        for index, value in enumerate(result):
            print(f"Корень {index} равен {value:0.3f}")


def do_work(a, b, c):
    print(f"Уравнение {a}x^2 + {b}x + {c} = 0 имеет следующие корни:")
    show_result(solve_square_eq(a, b, c))


def first_test():
    # test for 1 root
    assert len(solve_square_eq(1, 0, 0)) == 1
    assert solve_square_eq(1, 0, 0) == [0]
    print("Тест 1 пройден")


def third_test():
    # test for 2 roots
    assert len(solve_square_eq(1, 9, -36)) == 2
    # с произвольными действительными так не удобно
    assert solve_square_eq(1, 9, -36) == [3, -12]
    print("Тест 3 пройден")


def second_test():
    # test for 0 roots
    assert solve_square_eq(10, 1, 10) == []
    print("Тест 2 пройден")


if __name__ == "__main__":
    first_test()
    # second_test()
    third_test()
