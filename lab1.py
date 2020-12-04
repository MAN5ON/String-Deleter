unique = list()
remove_index = list()
hashes = set()

EQ = \
    {
        'o': 'о', 'e': 'е', 'p': 'р', 't': 'т', 'c': 'с', 'h': 'н',
        'a': 'а', 'x': 'х', 'k': 'к', 'b': 'в', 'm': 'м',
    }

EQreg = \
    {
        'o': 'о', 'a': 'а', 'e': 'е', 'c': 'с', 'p': 'р', 'x': 'х',
        'O': 'О', 'A': 'А', 'E': 'Е', 'C': 'С', 'P': 'Р', 'M': 'М',
        'B': 'В', 'X': 'Х', 'K': 'К', 'H': 'Н', 'T': 'Т'
    }


# Обе модификации вместе
def all(string: str):
    string = string.lower()
    for en, ru in EQ.items():
        string = string.replace(en, ru)

    return string


# Замена похожих символов из английского языка на русский
def natural(string: str):
    for en, ru in EQreg.items():
        string = string.replace(en, ru)

    return string


# Привод текста к одному регистру
def case(string: str):
    string = string.lower()

    return string


def helper():
    help = str('Алгоритм работы с программой:\n'
               '0. проверить путь к файлу, указанный в программе\n'
               '0.5 Указать свой путь к тестовым примерам и сохраняемым копиям\n'
               '1. Указать название файла\n'
               'Например : Test_10M_not_similar.txt\n'
               '2. Указать доп условие(если требуется)\n'
               '3. Дождаться выполнения\n'
               '4. Указать путь для сохранения копии файла с удалёнными повторяющимися строками\n'
               '---\n'
               'Модификации:\n'
               '  "-natural" – строки будут считаться одинаковыми, если они выглядят одинаково для человека\n'
               '  "-case" – приведение к одному регистру. Теперь большие и маленькие буквы будут считаться одинаковыми\n'
               '  "-all" - совмещение 2 предыдущих модификаций'
               '---\n')
    print(help)


def find_del():
    # Проверка условий
    with open(file, 'r', encoding="utf-8") as fp:
        data = fp.read()
        for ln_index, ln in enumerate(data.split('\n', )):
            if type(condition) not in [str]:
                raise TypeError('Ошибка! Неверный ввод команды')
                helper()
            elif condition in ['-case']:
                ln = case(ln)
            elif condition in ['-natural']:
                ln = natural(ln)
            elif condition in ['-all']:
                ln = all(ln)
            elif condition and not condition.isspace():
                raise ValueError('Ошибка! Неверный ввод команды')
                helper()

            # Поиск и внесение уникальных строк в список unique с помощью хэшей строк
            if ln not in hashes:
                hashes.add(ln)
                unique.append(ln)
            # Индекс удалённой строки
            else:
                remove_index.append(ln_index)


def save():
    exp = input(
        'Укажите название и расширение для сохранения ред. копии файла (файл сохранится в папке result)\n'
        'или нажмите Enter, чтобы вывести результат в консоль:\n')
    if exp and not exp.isspace():
        red = open(r'C:\projects\deletestring\result\''[:-1] + exp, 'w')
        # Запись уникальных строк в файл
        for value in unique:
            red.write(value + '\n')
        red.close()

    else:
        for value in unique:
            print(value + '\n')

    print('Индексы повторяющихся строк: ', remove_index)


print('Все тестовые файлы находятся в папке Examples')
inp = input('укажите название файла с типом(.txt):\n')
file = r'C:\projects\deletestring\examples\''[:-1] + inp
condition = input('Укажите одну из модификаций или оставьте поле пустым:\n').lower()
find_del()
save()
