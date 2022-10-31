def calc(text, log):
    try:
        return eval(text)
    except SyntaxError:
        log.error(f'model.calc Синтаксическая ошибка в {text}')
        return "Неверная формула"

def convert(kg, log):
    try:
        return int(kg) * 1000
    except ValueError:
        log.error(f'model.convert При конвертации {kg} в граммы возникла ошибка приведения к INT')
        return 'NaN'