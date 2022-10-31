def show_menu():
    print('1 - Калькулятор')
    print('2 - Конвертер')
    return input('Введите цифру: ')

def show_calc_enter():
    return input('Введите выражение: ')

def show_converter_enter():
    return input('Введите количество кг: ')


def show_calc_result(res):
    print('Результат калькуляции = ' + str(res))

def show_convert_result(res):
    print(f'{res[0]} кг = {res[1]} г')