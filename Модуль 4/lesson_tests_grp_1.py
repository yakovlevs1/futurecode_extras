from math import sqrt
import unittest

def solve_square_eq(a: float, b: float, c: float) -> list[float]:
    result = []

    disc = b ** 2 - 4 * a * c

    if disc == 0:
        result.append(-b / (2 * a))
    elif disc > 0: # else:
        result.append((-b + sqrt(disc)) / (2 * a))
        result.append((-b - sqrt(disc)) / (2 * a))

    return result

def show_result(data: list[float]):
    if len(data) > 0:
        #i = 1
        #for root in data:
        #    print(f"Корень номер {i} равен {root:.02f}")
        #    i += 1
        for index, value in enumerate(data):
            print(f"Корень номер {index+1} равен {value:.02f}")
    else:
        print("Уравнение с заданными параметрами не имеет корней над полем действительных чисел")


def main():
    a, b, c = map(float, input("Пожалуйста, введите три числа через пробел: ").split())
    result = solve_square_eq(a, b, c)
    show_result(result)


def some_test():
    # test for 1 root
    assert len(solve_square_eq(1, 0, 0)) == 1
    assert solve_square_eq(1, 0, 0) == [0.0]


class SqEqSolverTestCase(unittest.TestCase):
    def test_single_root(self):
        res = solve_square_eq(1, 0, 0)
        self.assertAlmostEqual(res[0], 0.0)
        self.assertEqual(len(res), 1)
    
    def test_sigle_root_with_not_zero_coefficients(self):
        res = solve_square_eq(10, -5, 0.625)
        self.assertAlmostEqual(res[0], 0.25)
        self.assertEqual(len(res), 1)
    
    def test_multiple_roots_case_Alex(self):
        res = solve_square_eq(2, 3, -5)
        self.assertEqual(len(res), 2)
        self.assertAlmostEqual(res, [1.0, -2.5])
    
    def test_zero_real_roots(self):
        res = solve_square_eq(2, -3, 2)
        self.assertEqual(len(res), 0)
        
        



if __name__ == "__main__":
    unittest.main()
    #main()
    #some_test()
