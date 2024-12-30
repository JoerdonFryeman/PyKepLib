import os
from time import sleep

from pykeplib import Base, Enigma, Visual, TextWork, DataProcessing, TheCPower, FileHandling

base = Base()
enigma = Enigma()
visual = Visual()
text_work = TextWork()
data_processing = DataProcessing()
the_c_power = TheCPower()
file_handling = FileHandling()


def coding_and_decoding_example():
    """Example of the coding and decoding functions"""
    enigma.get_method_info(
        'coding', f'was called and return: {enigma.coding('Hello world!')}'
    )
    enigma.get_method_info(
        'decoding', f'was called and return: {enigma.decoding('222406695695474553948474635695399736')}'
    )


@enigma.get_authentication_decorator(enigma.get_db_from_config(), 'pkl_sql.db')
def get_loading_points_example():
    """
    Example of the get_authentication_decorator and get_loading_points functions
    login: Kepler, password: 54
    """
    counter = 0
    for i in range(8):
        if counter == 4:
            counter = 0
        os.system(visual.select_os_command('clear_screen'))
        print(visual.get_loading_points('Loading', counter))
        counter += 1
        sleep(0.3)
    enigma.get_method_info('get_authentication_decorator', 'was called!')
    visual.get_method_info('get_loading_points', 'was called!')


@visual.loading_points_decorator()
def get_loading_points_example_decorator():
    """Example of the loading_points_decorator function"""
    visual.get_method_info('loading_points_decorator', 'will be called now!')


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
    visual.get_method_info('wake_up_neo', 'was called!')


def remove_symbols_example():
    """Example of the remove_symbols_return_word and remove_symbols_from_sentence functions"""
    text_work.logger.info(
        text_work.remove_symbols_return_word(
            f"deleted_Example of the method remove symbols return word._deleted",
            '_', 2
        )
    )
    text_work.logger.info(
        text_work.remove_symbols_from_sentence(
            f'Example_of_the_method_remove_symbols_from_sentence.', '_'
        ) + '\n'
    )
    text_work.get_method_info('remove_symbols_return_word', 'was called!')
    text_work.get_method_info('remove_symbols_from_sentence', 'was called!')


def get_random_data_example(user_data=(0, '1', 2, '3', 4, '5', 'Ω', 'λ', 'π', 'Σ', 'ω')):
    """Example of the get_random_data function"""
    random_data = data_processing.get_random_data()
    for i in range(61):
        if not random_data(user_data):
            continue
        print(f'Example of the function get_random_data: {random_data.__closure__[0].cell_contents}')
        sleep(0.3)
    data_processing.get_method_info('get_random_data', f'was called!')


def get_cubed(value: int):
    """Example of the get_exponentiation function"""
    cubed = the_c_power.get_exponentiation(value) * value  # cubed
    the_c_power.get_method_info('get_exponentiation', f'was called and return: {cubed}')


@the_c_power.get_exponentiation_decorator
def get_exponentiation_decorator(value: int):
    """Example of the get_exponentiation_decorator function"""
    the_c_power.get_method_info('get_exponentiation_decorator', f'was called and return: {value}')


def manipulate_with_script_in_file():
    """Example of the make_script_hidden_in_file and get_script_hidden_in_file functions"""
    file_handling.make_script_hidden_in_file('pykeplib', 'png', 'pykeplib', 'py')
    file_handling.get_method_info('make_script_hidden_in_file', 'was called!')
    file_handling.get_script_hidden_in_file('pykeplib_copy', 'png', 'pykeplib_copy', 'py', '60 82')
    file_handling.get_method_info('get_script_hidden_in_file', 'was called!')


def get_welcome_script():
    """Welcome script function"""
    print("\nYou are welcome at Kepler's personal library\nMore info you can find on https://github.com/JoerdonFryeman\n")


def main():
    """Entry point function"""
    try:
        get_welcome_script()
    except Exception as e:
        base.logger.error(f'Произошла непредвиденная ошибка: {e}')


if __name__ == '__main__':
    main()
