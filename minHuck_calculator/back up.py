if math_operation == '+':
    if 5 > numOfOperand > 3:
        result = int(operand_list[0]) + int(operand_list[1]) + int(operand_list[2]) + int(operand_list[3])
    elif 4 > numOfOperand > 2:
        result = int(operand_list[0]) + int(operand_list[1]) + int(operand_list[2])
    elif 3 > numOfOperand > 1:
        result = int(operand_list[0]) + int(operand_list[1])



elif math_operation == '-':
    if 5 > numOfOperand > 3:
        result = int(operand_list[0]) - int(operand_list[1]) - int(operand_list[2]) - int(operand_list[3])
    elif 4 > numOfOperand > 2:
        result = int(operand_list[0]) - int(operand_list[1]) - int(operand_list[2])
    elif 3 > numOfOperand > 1:
        result = int(operand_list[0]) - int(operand_list[1])
elif math_operation == '*':
    if 5 > numOfOperand > 3:
        result = int(operand_list[0]) * int(operand_list[1]) * int(operand_list[2]) * int(operand_list[3])
    elif 4 > numOfOperand > 2:
        result = int(operand_list[0]) * int(operand_list[1]) * int(operand_list[2])
    elif 3 > numOfOperand > 1:
        result = int(operand_list[0]) * int(operand_list[1])
elif math_operation == '%':
    if 5 > numOfOperand > 3:
        result = int(operand_list[0]) / int(operand_list[1]) / int(operand_list[2]) / int(operand_list[3])
    elif 4 > numOfOperand > 2:
        result = int(operand_list[0]) / int(operand_list[1]) / int(operand_list[2])
    elif 3 > numOfOperand > 1:
        result = int(operand_list[0]) / int(operand_list[1])