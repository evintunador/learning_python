from functools import singledispatch

class Expression:
    def __init__(self, operands):
        self.operands = operands

class Operator(Expression):
    symbol = ''
    precedence = 0

    def __repr__(self):
        return f"{type(self).__name__}{repr(self.operands)}"

    def __str__(self):
        operands_str = f" {self.symbol} ".join(
            str(operand) if operand.precedence >= self.precedence else f"({operand})"
            for operand in self.operands
        )
        return operands_str

class Terminal(Expression):
    precedence = float('inf')

    def __init__(self, value):
        super().__init__(())
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

class Add(Operator):
    symbol = '+'
    precedence = 1

    def __init__(self, left, right):
        super().__init__((left, right))

class Mul(Operator):
    symbol = '*'
    precedence = 2

    def __init__(self, left, right):
        super().__init__((left, right))

class Pow(Operator):
    symbol = '**'
    precedence = 3

    def __init__(self, left, right):
        super().__init__((left, right))

class Number(Terminal):
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Number value must be numeric")
        super().__init__(value)

class Symbol(Terminal):
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Symbol value must be a string")
        super().__init__(value)


@singledispatch
def evaluate(expr, variables):
    raise NotImplementedError(f"Evaluation not implemented for type {type(expr)}")

@evaluate.register
def _(expr: Number, variables):
    return expr.value

@evaluate.register
def _(expr: Symbol, variables):
    if expr.value in variables:
        return variables[expr.value]
    else:
        raise ValueError(f"Undefined symbol: {expr.value}")

@evaluate.register
def _(expr: Add, variables):
    left_value = evaluate(expr.operands[0], variables)
    right_value = evaluate(expr.operands[1], variables)
    return left_value + right_value

@evaluate.register
def _(expr: Mul, variables):
    left_value = evaluate(expr.operands[0], variables)
    right_value = evaluate(expr.operands[1], variables)
    return left_value * right_value

@evaluate.register
def _(expr: Pow, variables):
    left_value = evaluate(expr.operands[0], variables)
    right_value = evaluate(expr.operands[1], variables)
    return left_value ** right_value

# Construct the expression: 2 * y + 4 ^ (5 + x)
expr = Add(
    Mul(Number(2), Symbol('y')),
    Pow(Number(4), Add(Number(5), Symbol('x')))
)

# Define variable values
variables = {'x': 1, 'y': 2}

# Evaluate the expression
result = evaluate(expr, variables)
print(f"The result is: {result}")
