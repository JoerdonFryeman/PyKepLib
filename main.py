import os
from time import sleep
from pykeplib import Enigma, Visual, SymbolRemove, GetRandomData, TheCPower

enigma = Enigma()
visual = Visual()
sr = SymbolRemove()
rd = GetRandomData()
cp = TheCPower()


def coding_and_decoding_example():
    enigma.logger.info(
        f'Example of encoding a message using the method "coding": '
        f'{enigma.coding("Hello world!")}'
    )
    enigma.logger.info(
        f'Example of decoding a message using the method "decoding": '
        f'{enigma.decoding("222406695695474553948474635695399736")}'
    )


def get_loading_points_example():
    counter = 0
    while True:
        if counter == 4:
            counter = 0
        os.system(visual.get_system_command())
        visual.logger.info('example of the method usage "get_system_command"')
        visual.logger.info(visual.get_loading_points('Loading', counter))
        counter += 1
        sleep(0.3)


def remove_symbols_example():
    sr.logger.info(
        sr.remove_symbols_return_word(
            f"deleted_Example_deleted", '_', 2
        )
    )
    sr.logger.info(
        sr.remove_symbols_from_sentence(
            f'of_the_method_functional "remove_symbols_return_word"'
            f' и "remove_symbols_from_sentence"', '_'
        )
    )


def get_random_data_example():
    while True:
        x = rd.get_random_data((0, '1', 2, '3', 4, '5', 'Ω', 'λ', 'π', 'Σ', 'ω'))
        if not x:
            continue
        rd.logger.info(f'Example of the function "get_random_data": {x} | {rd.transfer_list}')
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
