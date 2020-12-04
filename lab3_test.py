import unittest

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


def all(string: str):
    string = string.lower()
    for en, ru in EQ.items():
        string = string.replace(en, ru)

    return string


def natural(string: str):
    for en, ru in EQreg.items():
        string = string.replace(en, ru)

    return string


# Привод текста к одному регистру
def case(string: str):
    string = string.lower()

    return string


def find_del(condition):
    with open(r'C:\projects\deletestring\examples\allegrova.txt', 'r', encoding="utf-8") as fp:
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



class TestStringMethods(unittest.TestCase):

    def test_options(self):
        self.assertEqual(all('CtPoKa TeKcTa'), 'строка текста')
        self.assertEqual(natural('CтPoKa TeKcTa'), 'СтРоКа ТеКсТа')
        self.assertEqual(case('СТРОКА ТЕКСТА'), 'строка текста')

    def test_findEValueErrors(self):
        self.assertRaises(ValueError,find_del, '-other command')
        self.assertRaises(ValueError, find_del, 'all')
        self.assertRaises(ValueError, find_del, '-natur')

    def test_findTypeError(self):
        self.assertRaises(TypeError, find_del, 19+2j)
        self.assertRaises(TypeError, find_del, True)
        self.assertRaises(TypeError, find_del, [42])
        self.assertRaises(TypeError, find_del, [42, 17])
