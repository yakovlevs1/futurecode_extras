from math import sqrt


def solve_square_eq(a: float, b: float, c: float) -> list[float]:
    result = []

    discr = b**2 - 4 * a * c

    if discr == 0:
        result.append(-b / (2 * a))
    else:#elif discr > 0:
        result.append((-b + sqrt(discr)) / (2 * a))
        result.append((-b - sqrt(discr)) / (2 * a))

    return result
