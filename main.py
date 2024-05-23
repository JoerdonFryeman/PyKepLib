import os
from time import sleep
from tests.tests import TestPyKepLib
from pykeplib import Enigma, Visual, SymbolRemove, GetRandomData, TheCPower

enigma = Enigma()
visual = Visual()
sr = SymbolRemove()
rd = GetRandomData()
test = TestPyKepLib()
cp = TheCPower()


def coding_and_decoding_example():
    enigma.logger.info(
        f'Пример кодирования сообщения с помощью метода "coding": '
        f'{enigma.coding("Hello world!")}'
    )
    enigma.logger.info(
        f'Пример декодирования сообщения с помощью метода "decoding": '
        f'{enigma.decoding("222406695695474553948474635695399736")}'
    )


def get_loading_points_example():
    counter = 0
    while True:
        if counter == 4:
            counter = 0
        os.system(visual.get_system_command())
        visual.logger.info('пример использования метода "get_system_command"')
        visual.logger.info(visual.get_loading_points('Загрузка', counter))
        counter += 1
        sleep(0.3)


def remove_symbols_example():
    sr.logger.info(
        sr.remove_symbols_return_word(
            f"удалено_Пример_удалено", '_', 2
        )
    )
    sr.logger.info(
        sr.remove_symbols_from_sentence(
            f'функционала_методов_"remove_symbols_return_word"'
            f' и "remove_symbols_from_sentence"', '_'
        )
    )


def get_random_data_example():
    while True:
        x = rd.get_random_data((0, '1', 2, '3', 4, '5', 'Ω', 'λ', 'π', 'Σ', 'ω'))
        if not x:
            continue
        rd.logger.info(f'Пример работы функции "get_random_data": {x} | {rd.transfer_list}')
        sleep(0.3)


def get_cubed(value):
    cubed = cp.get_exponentiation(value) * value
    print(cubed)


def get_welcome_script():
    print("\nYou are welcome at Kepler's personal library\nMore info you can find on https://github.com/kepler54\n")


def main():
    get_welcome_script()


if __name__ == '__main__':
    main()
