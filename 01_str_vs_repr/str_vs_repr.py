# learning the difference between repr & str
class Polynomial():
    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients)-1

print("No str or repr")
g = Polynomial((1,2,3))
print(g)
print('str()', str(g))
print('repr()', repr(g))
print(f'in an f-string it looks like {g}')
print(f'f-string using the !r modifier {g!r}')
print('-'*20)

class Polynomial():
    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients)-1
    
    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"
    # we use type(self).__name__ rather than hard-typing-out the class's name bc this class may be
    # inherited by another down the line, in which case its name would change

print("Using repr")
g = Polynomial((1,2,3))
print(g)
print('str()', str(g))
print('repr()', repr(g))
print(f'in an f-string it looks like {g}')
print(f'f-string using the !r modifier {g!r}')
print('-'*20)

class Polynomial():
    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients)-1

    def __str__(self):
        terms = []

        # Degree 0 and 1 terms conventionally have different representation.
        if self.coefficients[0]:
            terms.append(str(self.coefficients[0]))
        if self.degree() > 0 and self.coefficients[1]:
            terms.append(f"{self.coefficients[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                for d, c in enumerate(self.coefficients[2:], start=2) if c]

        # Sum Polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

print("Using str")
g = Polynomial((1,2,3))
print(g)
print('str()', str(g))
print('repr()', repr(g))
print(f'in an f-string it looks like {g}')
print(f'f-string using the !r modifier {g!r}')
print('-'*20)

class Polynomial():
    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients)-1
    
    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"

    def __str__(self):
        terms = []

        # Degree 0 and 1 terms conventionally have different representation.
        if self.coefficients[0]:
            terms.append(str(self.coefficients[0]))
        if self.degree() > 0 and self.coefficients[1]:
            terms.append(f"{self.coefficients[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                for d, c in enumerate(self.coefficients[2:], start=2) if c]

        # Sum Polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

print("Using both")
g = Polynomial((1,2,3))
print(g)
print('str()', str(g))
print('repr()', repr(g))
print(f'in an f-string it looks like {g}')
print(f'f-string using the !r modifier {g!r}')
print('-'*20)

# convention-wise, what you're supposed to do is use str() for a pretty 
# output and use repr() for writing out a demonstration to the user of 
# what they should type in order to define an object like this