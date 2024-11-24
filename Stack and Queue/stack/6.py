def evalRPN(tokens):
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Use int() to truncate towards zero
        else:
            stack.append(int(token))
    
    return stack[-1]

print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9

print(evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6

print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22
