def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_operands = []
    second_operands = []
    operators = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            continue
        
        first_operand, operator, second_operand = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        
        if operator == '+':
            answer = str(int(first_operand) + int(second_operand))
        else:
            answer = str(int(first_operand) - int(second_operand))
        answers.append(answer)
    
    top_row = ""
    bottom_row = ""
    lines = ""
    answer_row = ""
    
    for i in range(len(first_operands)):
        first_operand = first_operands[i]
        second_operand = second_operands[i]
        operator = operators[i]
        answer = answers[i]
        
        length = max(len(first_operand), len(second_operand)) + 2
        top_row += first_operand.rjust(length)
        bottom_row += operator + second_operand.rjust(length - 1)
        lines += "-" * length
        answer_row += answer.rjust(length)
        
        if i < len(first_operands) - 1:
            top_row += "    "
            bottom_row += "    "
            lines += "    "
            answer_row += "    "
    
    if display_answers:
        arranged_problems = f"{top_row}\n{bottom_row}\n{lines}\n{answer_row}"
    else:
        arranged_problems = f"{top_row}\n{bottom_row}\n{lines}"
    
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
