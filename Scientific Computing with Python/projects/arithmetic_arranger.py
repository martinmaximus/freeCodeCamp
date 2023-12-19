
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
operators = ["+", "-"]
first_number = []
second_number = []
result = []


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in problems:
        first_number, operator, second_number = problem.split()
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)

        length = max(len(first_number), len(second_number)) + 2
        first_line += first_number.rjust(length)
        second_line += operator + second_number.rjust(length - 1)
        third_line += "-" * length
        fourth_line += str(result).rjust(length)

        if problem != problems[-1]:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "

    if solve:
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line

    return arranged_problems

arithmetic_arranger(problems, solve=True)

print(arithmetic_arranger(problems, solve=True))