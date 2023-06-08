import unittest
from math import sqrt


def square_eq_solver(a, b, c):
    result = []
    discriminant = b * b - 4 * a * c

    if discriminant == 0:
        result.append(-b / (2 * a))

    else:    # elif discriminant > 0:  # <--- изменили условие, теперь
        # при нулевом дискриминанте
        # не будут вычисляться корни
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))

    return result


def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f"Корень номер {index+1} равен {value:.02f}")
    else:
        print("Уравнение с заданными параметрами не имеет корней")


def main():
    a, b, c = map(int, input("Пожалуйста, введите три числа через пробел: ").split())
    result = square_eq_solver(a, b, c)
    show_result(result)


class SquareEqSolverTestCase(unittest.TestCase):
    def test_no_root(self):
        res = square_eq_solver(10, 0, 2)
        self.assertEqual(len(res), 0)

    def test_single_root(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [0.5, -3])


if __name__ == "__main__":
    unittest.main()
