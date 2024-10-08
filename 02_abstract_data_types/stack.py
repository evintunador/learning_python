# a sequence of objects in which only the most recently added object is accessible
# alternative name for a stack is a LIFO (last in, first out)
# The operations are push to add a new object to the sequence, 
#   and pop to return the most recently added object, and remove it from the sequence
# operation of peek, which returns the most recently added object without removing it

class Stack():
    def __init__(self, stack_list):
        assert isinstance(stack_list, list), 'input must be of type list'
        self.stack = stack_list

    def push(self, x): # add x to the top of the stack
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() # python lists already have a .pop()
    
    def peek(self):
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.peek())
    
stack = Stack([1,2,3])
print(stack)
stack.push(4)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())

# In reverse Polish notation, the operator follows its operands. 
# For example to add the numbers one and two, one would write 1 2 +. 
# Formally, a reverse Polish calculator comprises a set of numbers, 
#   a set of operators (each of which takes a fixed number of arguments), 
#   and a stack. 
# Each number encountered in the expression is pushed onto the stack, 
#   while each operator pops the right number of arguments off the stack 
#   and pushes the result onto the stack. 
# At the end of the calculation, the result is on the top of the stack

import operator

def polish(equation):
    """evaluates lists of integers * str(operators) in polish notation"""
    stack = Stack([])
    operators = ['+', '-', '*', '/', '//', '%', '**']

    def string_to_operator(op_string):
        """turns strings of operators into actual callabe operators"""
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '//': operator.floordiv,
            '%': operator.mod,
            '**': operator.pow
        }
        return ops.get(op_string)

    for item in equation:
        if isinstance(item, int):
            stack.push(item)
        elif item in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            op = string_to_operator(item)
            sub_result = op(operand1, operand2)
            stack.push(sub_result)

    return stack.pop()

equation = [6, 2, '/', 2, 4, '**', '+']
print(equation)
output = polish(equation)
print(output)