# The character * is the argument packing operator, also known as the splat operator
# When used in the parameter list of a function, splat takes all of the remaining 
# positional arguments provided by the caller and packs them up in a tuple

a = (1,2,3)
print(*a)
# which is identical to
print(1,2,3)
# but different from
print(a)

# The double splat operator, ** plays a similar role to the single splat operator, 
# but packs and unpacks keyword arguments instead of positional arguments. 
# When used in the parameter list of a function, ** gathers all of the 
# keyword arguments that the caller passes, other than any which are explicitly 
# named in the interface. The result is a dict whose keys are the argument names, 
# and whose values are the arguments

def fn(a, b, **kwargs):
    print("a:", a)
    print("b:", b)
    print("kwargs:", kwargs)

fn(1, f=3, b=2, g="hello")

# Combining the splat and double splat operators, it is possible to write a 
# function that will accept any combination of positional and keyword arguments.
# This is often useful if the function is intended to pass these arguments 
# through to another function, without knowing anything about that inner function

fn(*args, **kwargs):
    a =  inner_fn(*args, **kwargs)

# The names *args and **kwargs are the conventional names in cases where nothing 
# more specific is known about the parameters in question.