from math import trunc
def do_op(first, second, op):
    print(f"DOING {first} {op} {second}")
    if op == "+":
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    elif op == "/":
        return trunc(first / second)
    else:
        raise Exception("INVALID OP")

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    num_stack = []


    for s in tokens:
        if s not in ["+", "-", "*", "/"]:
            num_stack.append(int(s))
        else:
            n1 = num_stack.pop()
            n2 = num_stack.pop()
            res = do_op(n2, n1, s)
            num_stack.append(int(res))
    
    if len(num_stack) != 1:
        print("BUG")
    return num_stack[-1]



tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))

