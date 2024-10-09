def postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():  # if the token is an operand (number)
            stack.append(int(token))
        else:  # if the token is an operator
            operand2 = stack.pop()  # pop the top two operands
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2  # for division, use float division
            stack.append(result)  # push the result back onto the stack

    return stack[0]  # the final result will be the only element in the stack


input_expression = ["2", "1", "+", "4", "*"]
result = postfix(input_expression)
print("Postfix expression result:", result)