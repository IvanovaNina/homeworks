import logger

expression = ''
result = None


def set_expression(expr):
    global expression
    expression = expr


def set_result(res):
    global result
    result = res


def get_expression():
    global expression
    return expression


def get_result():
    global result
    return result


def calculate():
    items = parse()
    intermediate_results = []
    skip_next = False
    for i in range(len(items)):
        if not skip_next:
            if items[i] == '*' or items[i] == '/':
                idx = len(intermediate_results) - 1
                res = operate(intermediate_results[idx], items[i + 1], items[i])
                logger.info(intermediate_results[idx], items[i + 1], items[i], res)
                intermediate_results[idx] = res
                skip_next = True
            else:
                intermediate_results.append(items[i])
        else:
            skip_next = False

    intermediate_result = intermediate_results[0]
    for i in range(len(intermediate_results) - 1):
        if intermediate_results[i] == '+' or intermediate_results[i] == '-':
            res = operate(intermediate_result, intermediate_results[i + 1], intermediate_results[i])
            logger.info(intermediate_result, intermediate_results[i + 1], intermediate_results[i], res)
            intermediate_result = res
    set_result(intermediate_result)


def operate(first_number, second_number, operator):
    if first_number and second_number:
        if operator == '+':
            return first_number + second_number
        elif operator == '-':
            return first_number - second_number
        elif operator == '*':
            return first_number * second_number
        elif operator == '/':
            return first_number / second_number


def parse():
    items = []
    numeric_str = ''
    for str in get_expression():
        if str == '.':
            numeric_str += str
        elif is_operator(str):
            items.append(to_float(numeric_str))
            numeric_str = ''
            items.append(str)
        else:
            numeric_str += str
    items.append(to_float(numeric_str))
    return items


def is_operator(str):
    return str == '*' or str == '/' or str == '+' or str == '-'


def to_float(value):
    if value is None:
        return ''
    try:
        return float(value)
    except:
        return ''
