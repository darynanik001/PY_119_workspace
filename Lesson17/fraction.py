class Fraction:
    def __init__(self, op1: float, op2: float):
        if not isinstance(op1, float | int) or not isinstance(op2, float | int):
            raise TypeError("Not a number")
        self.op1 = op1
        self.op2 = op2

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Not a fraction")
        return Fraction(self.op1 + other.op1, self.op2 + other.op2)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Not a fraction")
        return Fraction(self.op1 - other.op1, self.op2 - other.op2)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Not a fraction")
        return Fraction(self.op1 * other.op1, self.op2 * other.op2)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Not a fraction")
        return self.op1 == other.op1 and self.op2 == other.op2

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Not a fraction")

        try:
            return Fraction(self.op1 / other.op1, self.op2 / other.op2)
        except ZeroDivisionError:
            return f"Division by 0 is not allowed."


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 0)
    print(x + y == Fraction(2, 6))

    print(x / y)
