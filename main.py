import os
import curses
from time import sleep
from pykeplib import Enigma, Visual, SymbolRemove, GetRandomData, TheCPower


# reset to save 21

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


def get_wake_up_neo_text():
    curses.wrapper(visual.wake_up_neo, ['Wake up, Neo...', 'The Matrix has you...', 'Follow the white rabbit.'])

    def get_extra_text(stdscr):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        GREEN_ON_BLACK = curses.color_pair(1)
        stdscr.clear()
        stdscr.addstr(2, 3, 'Knock, knock, Neo.', GREEN_ON_BLACK)
        stdscr.refresh()
        sleep(4.2)
        stdscr.clear()

    curses.wrapper(get_extra_text)

    def get_user_text():
        sentences_list = []
        enter = True
        while enter:
            enter = input('Enter your sentence: ')
            sentences_list.append(enter)
        curses.wrapper(visual.wake_up_neo, sentences_list)
        os.system(visual.get_system_command())

    get_user_text()


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


@cp.get_exponentiation_decorator
def get_exponentiation_example(value):
    print(value)


@visual.loading_points_decorator
def get_cubed_example(value):
    cubed = cp.get_exponentiation(value) * value
    print(cubed)


def get_welcome_script():
    print("\nYou are welcome at Kepler's personal library\nMore info you can find on https://github.com/kepler54\n")


def main():
    get_welcome_script()


if __name__ == '__main__':
    main()
