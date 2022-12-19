import model
import view


def start():
    expression = ''
    while expression != 'q':
        expression = view.input_expt_string()
        model.set_expression(expression)
        model.calculate()
        view.print_result(model.get_result())
