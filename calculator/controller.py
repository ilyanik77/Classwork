from statistics import mode
import model
import view


def run(log):
    log.info('Показываю меню')
    option = view.show_menu()
    log.warn('Меню показано')
    if option == '1':
        log.info('Выбран калькулятор')
        res = view.show_calc_enter()
        res = model.calc(res, log)
        view.show_calc_result(res)

    if option == '2':
        log.info('Выбран конвертер')
        kg = view.show_converter_enter()
        res = model.convert(kg, log)
        view.show_convert_result([kg, res])