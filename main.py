import os
from time import sleep
from pykeplib import System, Enigma, Visual, SymbolRemove, GetRandomData

sy = System()
en = Enigma()
vi = Visual()
sr = SymbolRemove()
rd = GetRandomData()


def coding_and_decoding_example():
    print(
        f'\nПример кодирования сообщения с помощью метода "coding": '
        f'{en.coding("Hello world!")}\n'
    )
    print(
        f'Пример декодирования сообщения с помощью метода "decoding": '
        f'{en.decoding("222406695695474553948474635695399736")}\n'
    )


def get_loading_points_example():
    counter = 0
    while True:
        if counter == 4:
            counter = 0
        counter += 1

        os.system(sy.get_system_command())  # пример использования метода get_system_command

        print(vi.get_loading_points('Загрузка', counter))
        sleep(0.3)


def remove_symbols_example():
    print(
        sr.remove_symbols_return_word(
            f"удалено_\nПример_удалено", "_", 2
        ), end=''
    )
    print(
        sr.remove_symbols_from_sentence(
            f'_функционала_методов_"remove_symbols_return_word"'
            f' и "remove_symbols_from_sentence"\n', '_'
        )
    )


def get_random_data_example():
    while True:
        x = rd.get_random_data((0, '1', 2, '3', 4, '5', 'Ω', 'λ', 'π', 'Σ', 'ω'))
        if not x:
            continue
        print(f'Пример работы функции "get_random_data": {x} | {rd.transfer_list}')
        sleep(0.3)


def main():
    pass


if __name__ == '__main__':
    main()
