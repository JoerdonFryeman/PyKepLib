import os
from time import sleep
from pykeplib import Enigma, Visual, SymbolRemove, GetRandomData, TheCPower

enigma = Enigma()
visual = Visual()
sr = SymbolRemove()
rd = GetRandomData()
cp = TheCPower()


def coding_and_decoding_example():
    """Example of the coding and decoding functions"""
    enigma.logger.info(
        f'Example of encoding a message using the method "coding": '
        f'{enigma.coding("Hello world!")}'
    )
    enigma.logger.info(
        f'Example of decoding a message using the method "decoding": '
        f'{enigma.decoding("222406695695474553948474635695399736")}'
    )


@enigma.get_authentication_decorator(enigma.get_db_from_config(), 'pkl_sql.db')
def get_loading_points_example():
    """
    Example of the get_authentication_decorator and get_loading_points functions
    login: Kepler, password: 54
    """
    counter = 0
    while True:
        if counter == 4:
            counter = 0
        os.system(visual.select_os_command('clear_screen'))
        print(visual.get_loading_points('Loading', counter))
        counter += 1
        sleep(0.3)


@visual.loading_points_decorator(8, 'loading')
def get_loading_points_example_decorator():
    """Example of the loading_points_decorator function"""
    pass


def get_wake_up_neo_text():
    """Example of the wake_up_neo function"""
    visual.wake_up_neo(['Wake up, Neo...', 'The Matrix has you...', 'Follow the white rabbit.'])
    os.system(visual.select_os_command('clear_screen'))
    print('Knock, knock, Neo.')
    sleep(4.2)
    os.system(visual.select_os_command('clear_screen'))

    def get_user_text():
        sentences_list, enter = [], True
        while enter:
            enter = input('Enter your sentence: ')
            sentences_list.append(enter)
        visual.wake_up_neo(sentences_list)

    get_user_text()


def remove_symbols_example():
    """Example of the remove_symbols_return_word and remove_symbols_from_sentence functions"""
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


def get_random_data_example(user_data=(0, '1', 2, '3', 4, '5', 'Ω', 'λ', 'π', 'Σ', 'ω')):
    """Example of the get_random_data function"""
    random_data = rd.get_random_data()
    while True:
        if not random_data(user_data):
            continue
        print(f'Example of the function "get_random_data": {random_data.__closure__[0].cell_contents}')
        sleep(0.3)


def get_cubed(value: int):
    """Example of the get_exponentiation function"""
    cubed = cp.get_exponentiation(value) * value
    print(cubed)


@cp.get_exponentiation_decorator
def get_exponentiation_decorator(value: int):
    """Example of the get_exponentiation_decorator function"""
    print(value)


def manipulate_with_script_in_file():
    """Example of the make_script_hidden_in_file and get_script_hidden_in_file functions"""
    visual.make_script_hidden_in_file('pykeplib', 'png', 'pykeplib', 'py')
    visual.get_script_hidden_in_file('pykeplib_copy', 'png', 'pykeplib_copy', 'py', '60 82')


def get_welcome_script():
    """Welcome script function"""
    print("\nYou are welcome at Kepler's personal library\nMore info you can find on https://github.com/kepler54\n")


def main():
    """Entry point function"""
    get_welcome_script()


if __name__ == '__main__':
    main()
