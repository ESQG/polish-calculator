"""Calculator

    >>> calc("+ 1 2") == 3  # 1 + 2
    True

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2") == 3 # 6 / (4 - 2)
    True
"""

def add(old, new):
    return old + new


def subtract(old, new):
    return new - old


def multiply(old, new):
    return old * new


def divide(old, new):
    quotient = float(new) / old
    if quotient == int(quotient):
        return int(quotient)
    return quotient

     
def is_num(s):

    return type(s) in {int, float, long} or s.isdigit() or s[1:].isdigit()


def calc(s):
    """Evaluate expression."""

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        }

    all_info = s.split()

    stack = [all_info[0]]

    for item in all_info[1:]:
        holding_variable = item

        while len(stack) > 0 and is_num(stack[-1]) and is_num(holding_variable):
            old_num = int(holding_variable)
            new_num = int(stack.pop())
            operator = stack.pop()

            holding_variable = operations[operator](old_num, new_num)
        
        stack.append(holding_variable)


    return holding_variable



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
