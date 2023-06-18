import unittest
from main import solve_square_eq


class TestSqEqSolver(unittest.TestCase):
    def test_single_root_zero(self):
        res = solve_square_eq(10, 0, 0)
        self.assertAlmostEqual(res[0], 0.0, delta=0.000001)
        self.assertEqual(len(res), 1)

    def test_single_root(self):
        res = solve_square_eq(1, -2, 1)
        self.assertAlmostEqual(res[0], 1.0, delta=0.000001)
        self.assertEqual(len(res), 1)

    def test_multiple_roots(self):
        res = solve_square_eq(2, 3, -5)
        self.assertEqual(len(res), 2)
        self.assertAlmostEqual(res[0], 1.1, delta=0.000001)
        self.assertAlmostEqual(res[1], -2.5, delta=0.000001)

    def test_zero_real_roots(self):
        #self.assertRaises(ValueError, solve_square_eq, 2, -3, 2)
        res = solve_square_eq(2, -3, 2)
        self.assertEqual(len(res), 0)

if __name__ == "__main__":
    unittest.main()
