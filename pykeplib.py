import os
from ctypes import *
from json import load
from time import sleep
from platform import system
from random import choice, randint
from logging import config, getLogger


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Base:
    @staticmethod
    def get_json_data(name: str) -> dict:
        try:
            with open(f'{name}.json', encoding='UTF-8') as file:
                data = load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError('File not found!')

    config.dictConfig(get_json_data('logging'))
    logger = getLogger()


class CKepLib(Base):
    @staticmethod
    def _get_cdll():
        try:
            return CDLL('./ckeplib.so')
        except OSError:
            raise OSError('OS Error!')


class PyKepLib(Base):
    def __create_coding_or_decoding_dict(self):
        try:
            coding_or_decoding_dict = (
                self.get_json_data('coding_or_decoding_dict/coding_dict_zero'),
                self.get_json_data('coding_or_decoding_dict/coding_dict_one'),
                self.get_json_data('coding_or_decoding_dict/decoding_dict_two'),
                self.get_json_data('coding_or_decoding_dict/decoding_dict_three')
            )
            return coding_or_decoding_dict
        except FileNotFoundError:
            raise FileNotFoundError('File not found!')

    @property
    def get_coding_or_decoding_dict(self):
        return self.__create_coding_or_decoding_dict

    @staticmethod
    def get_system_command() -> str:
        return {'Linux': lambda: 'clear', 'Windows': lambda: 'cls'}[system()]()

    def make_script_hidden_in_file(self, f_name: str, f_format: str, s_name: str, s_format: str):
        """
        The function makes the script hidden in the file
        :param f_name: name of the file
        :param f_format: files format
        :param s_name: name of the script
        :param s_format: scripts format
        """
        try:
            with (
                open(f'{f_name}.{f_format}', 'rb') as file,
                open(f'{f_name}_copy.{f_format}', 'wb') as file_copy
            ):
                file_copy.write(file.read())
            self.logger.info(f'The {f_name}.{f_format} file was copied!')
            with (
                open(f'{f_name}_copy.{f_format}', 'ab') as file_for_script,
                open(f'{s_name}.{s_format}', 'rb') as file_with_script
            ):
                file_for_script.write(file_with_script.read())
            self.logger.info(
                f'To the {f_name}_copy.{f_format} file was a hidden script '
                f'{s_name}.{s_format} written!'
            )
        except FileNotFoundError:
            self.logger.error('File not found!')

    def get_script_hidden_in_file(self, f_name: str, f_format: str, s_name: str, s_format: str, f_bytes: str):
        """
        The function pulls a hidden script from a file
        :param f_name: name of the file
        :param f_format: files format
        :param s_name: name of the script
        :param s_format: scripts format
        :param f_bytes: name of the bytes
        """
        try:
            with open(f'{f_name}.{f_format}', 'rb') as file:
                content = file.read()
                offset = content.index(bytes.fromhex(f_bytes))  # 'FF D9'
                file.seek(offset + 2)
                with open(f'{s_name}.{s_format}', 'wb') as new_file:
                    new_file.write(file.read())
            self.logger.info(
                f'From the {f_name}.{f_format} file was a hidden script '
                f'{s_name}.{s_format} pulled out!'
            )
        except FileNotFoundError:
            self.logger.error('File not found!')
        except ValueError:
            self.logger.error('Subsection not found!')


class TheCPower(CKepLib):
    def get_exponentiation(self, value):
        return self._get_cdll().main(value)

    def get_exponentiation_decorator(self, func):
        def wrapper(*args):
            return func(self._get_cdll().main(*args))

        return wrapper


class Visual(PyKepLib):
    @staticmethod
    def get_loading_points(text: str, counter: int) -> str:
        """
        The method takes the counter value as a dictionary key and
        returns different number of points for different counter values.
        :param text: user text
        :param counter: counter of the points
        :return: text with the points
        """
        if counter == 0:
            return f'{text}   '
        elif counter == 1:
            return f'{text}.  '
        elif counter == 2:
            return f'{text}.. '
        elif counter == 3:
            return f'{text}...'

    def loading_points_decorator(self, func, text='Loading'):
        def wrapper(*args):
            counter, result = 0, func(*args)
            for i in range(4):
                if counter == 4:
                    counter = 0
                dictionary = {
                    0: lambda x: f'{text}   ', 1: lambda x: f'{text}.  ',
                    2: lambda x: f'{text}.. ', 3: lambda x: f'{text}...',
                }[counter](text)
                os.system(self.get_system_command())
                print(dictionary)
                counter += 1
                sleep(0.3)
            return result

        return wrapper

    def wake_up_neo(self, sentences_list: list):
        """
        The function takes a list of words and return as a printed input
        :param sentences_list: list of user sentences
        """
        _counter_first = 0
        for text in sentences_list:
            _counter_first += 1
            _counter_second = 0
            sentence = [i for i in text]
            for i in range(len(sentence)):
                _counter_second += 1
                match _counter_first:
                    case 1:
                        sleep(float(f'0.{randint(1, 3)}'))
                    case 2:
                        sleep(float(f'0.{randint(2, 4)}'))
                    case 3:
                        sleep(float(f'0.{randint(1, 3)}'))
                    case _:
                        sleep(float(f'0.{randint(randint(1, 2), randint(3, 4))}'))
                os.system(self.get_system_command())
                print(''.join(sentence[0:_counter_second]))
            sleep(float(4))


class Enigma(PyKepLib):
    def coding(self, text: str | int | float) -> str:
        """
        The method accepts string or numeric information and
        returns it in encoded string form.
        :param text: user text or numbers or symbols
        :return: encoded string
        """
        try:
            dict_zero = [self.get_coding_or_decoding_dict()[0][i] for i in [i for i in text]]
            dict_one = [self.get_coding_or_decoding_dict()[1][i] for i in [i for i in dict_zero]]
            return ''.join(dict_one)
        except KeyError:
            self.logger.error('Encoding error!')

    def decoding(self, code: str | int | float) -> str:
        """
        The method accepts a string or numeric code and
        returns information in decoded string form.
        :param code: encoded string
        :return: decoded string of text, numbers or symbols
        """
        try:
            _counter = 0
            transfer_first = []
            for i in range(len(str(code)) // 3):
                transfer_first.append(''.join(str(code)[_counter:3 + _counter]))
                _counter += 3
            dict_two = [self.get_coding_or_decoding_dict()[2][i] for i in transfer_first]
            dict_three = [self.get_coding_or_decoding_dict()[3][i] for i in dict_two]
            return ''.join(dict_three)
        except KeyError:
            self.logger.error('Encoding error!')


class GetRandomData(PyKepLib):
    @staticmethod
    def get_random_data():
        """
        The method accepts a list or tuple of objects, adds them to the transfer_list
        with the help of a loop of GetRandomData class and returns them in random order without repeating.
        :return: random data without repeating
        """
        transfer_list = []

        def inner_function(inner_data: list | tuple) -> str | int | float:
            try:
                choice_data = choice(inner_data)
                if choice_data not in transfer_list:
                    transfer_list.append(choice_data)
                    if len(transfer_list) == len(inner_data):
                        transfer_list.clear()
                    return choice_data
                else:
                    return ''
            except ValueError:
                pass

        return inner_function


class SymbolRemove(PyKepLib):
    # You can use regular expressions from the built-in library re for example:
    # re.sub(r'\bWord_first\b', 'Word_second', str)
    # re.findall(r'\d{4}', str)
    # re.split(r'\W+', str)

    def remove_symbols_return_word(self, word_with_symbol: str, removed_symbol: str, word_number: int) -> str:
        """
        The method removes from a word or sentence a character accepted in string form and
        returns the word selected by the third parameter as a number.
        :param word_with_symbol: user word or sentence
        :param removed_symbol: symbol must be removed
        :param word_number: number of the word position
        :return: word
        """
        try:
            return (''.join(word_with_symbol)).split(removed_symbol)[word_number - 1]
        except (TypeError, IndexError, ValueError):
            self.logger.error('Invalid input!')

    def remove_symbols_from_sentence(self, suggestion: str, removed_symbol: str) -> str:
        """
        The method removes a character from a word or sentence accepted as a string
        second parameter and returns this word or sentence.
        :param suggestion: user word or sentence
        :param removed_symbol: symbol must be removed
        :return: word or sentence
        """
        try:
            return ' '.join(suggestion.split(removed_symbol))
        except (TypeError, AttributeError, ValueError):
            self.logger.error('Invalid input!')
