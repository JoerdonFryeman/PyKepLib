import os
import json
from ctypes import *
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
            with open(f'{name}.json') as file:
                data = json.load(file)
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
    @staticmethod
    def _split_text(text):
        return [i for i in text]

    def __create_coding_or_decoding_dict(self):
        try:
            coding_or_decoding_dict = [
                self.get_json_data('coding_or_decoding_dict/coding_dict_zero'),
                self.get_json_data('coding_or_decoding_dict/coding_dict_one'),
                self.get_json_data('coding_or_decoding_dict/decoding_dict_two'),
                self.get_json_data('coding_or_decoding_dict/decoding_dict_three')
            ]
            return coding_or_decoding_dict
        except FileNotFoundError:
            raise FileNotFoundError('File not found!')

    @property
    def get_coding_or_decoding_dict(self):
        return self.__create_coding_or_decoding_dict

    @staticmethod
    def get_system_command() -> str:
        system_name = system()
        if system_name == 'Linux':
            return 'clear'
        elif system_name == 'Windows':
            return 'cls'


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

        :param text: str
        :param counter: int
        :return: str
        """
        if int(counter) == 0:
            return f'{text}'
        elif int(counter) == 1:
            return f'{text}.'
        elif int(counter) == 2:
            return f'{text}..'
        elif int(counter) == 3:
            return f'{text}...'

    def loading_points_decorator(self, func, text='Loading'):
        def wrapper(*args):
            counter = 0
            result = func(*args)
            for i in range(4):
                if counter == 4:
                    counter = 0
                dictionary = {
                    0: lambda x: f'{text}   ',
                    1: lambda x: f'{text}.  ',
                    2: lambda x: f'{text}.. ',
                    3: lambda x: f'{text}...',
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

        :param sentences_list: list
        """
        counter_first = 0
        for s in sentences_list:
            counter_first += 1
            counter_second = 0
            sentence = [i for i in str(s)]
            for i in range(len(sentence)):
                counter_second += 1
                if counter_first == 1:
                    sleep(float(f'0.{randint(1, 3)}'))
                elif counter_first == 2:
                    sleep(float(f'0.{randint(2, 4)}'))
                elif counter_first == 3:
                    sleep(float(f'0.{randint(1, 3)}'))
                os.system(self.get_system_command())
                print(''.join(sentence[0:counter_second]))
            sleep(float(4))


class Enigma(PyKepLib):
    def coding(self, text: str | int | float) -> str:
        """
        The method accepts string or numeric information and
        returns it in encoded string form.

        :param text: str or int
        :return: str
        """
        try:
            transfer_first = []
            transfer_second = []

            for i in self._split_text(str(text)):
                transfer_first.append(self.get_coding_or_decoding_dict()[0][i])
            for i in self._split_text(''.join(transfer_first)):
                transfer_second.append(self.get_coding_or_decoding_dict()[1][i])

            return ''.join(transfer_second)

        except KeyError:
            self.logger.error('Encoding error!')

    def decoding(self, code: str | int | float) -> str:
        """
        The method accepts a string or numeric code and
        returns information in decoded string form.

        :param code: str or int
        :return: str
        """
        try:
            iteration_value = len(str(code))
            counter = 0

            transfer_first = []
            transfer_second = []
            transfer_third = []

            for i in range(iteration_value // 3):
                transfer_first.append(''.join(str(code)[counter:3 + counter]))
                counter += 3
            for i in transfer_first:
                transfer_second.append(self.get_coding_or_decoding_dict()[2][i])
            for i in transfer_second:
                transfer_third.append(self.get_coding_or_decoding_dict()[3][i])

            return ''.join(transfer_third)

        except KeyError:
            self.logger.error('Encoding error!')


class GetRandomData(PyKepLib):
    transfer_list = []

    def get_random_data(self, data_list: list | tuple | set) -> str:
        """
        The method accepts a list or tuple of objects, adds them to the transfer_list
        with the help of a loop of GetRandomData class and returns them in random order without repeating.

        :param data_list: list
        :return: str
        """
        try:
            data = choice(list(data_list) or tuple(data_list))
            if data not in self.transfer_list:
                self.transfer_list.append(data)
                if len(self.transfer_list) == len(data_list):
                    self.transfer_list.clear()
                return data
            else:
                return ''
        except ValueError:
            pass


class SymbolRemove(PyKepLib):
    def remove_symbols_return_word(self, word_with_symbol: str, removed_symbol: str, word_number: int) -> str:
        """
        The method removes from a word or sentence a character accepted in string form and
        returns the word selected by the third parameter as a number.

        :param word_with_symbol: str
        :param removed_symbol: str
        :param word_number: int
        :return: str
        """
        try:
            return (''.join(word_with_symbol)).split(removed_symbol)[word_number - 1]
        except (TypeError, IndexError, ValueError):
            self.logger.error('Invalid input!')

    def remove_symbols_from_sentence(self, suggestion: str, removed_symbol: str) -> str:
        """
        The method removes a character from a word or sentence accepted as a string
        second parameter and returns this word or sentence.

        :param suggestion: str
        :param removed_symbol: str
        :return: str
        """

        # You can use regular expressions from the built-in library re for example:
        # re.sub(r'\bWord_first\b', 'Word_second', str)
        # re.findall(r'\d{4}', str)
        # re.split(r'\W+', str)

        try:
            return ' '.join(suggestion.split(removed_symbol))
        except (TypeError, AttributeError, ValueError):
            self.logger.error('Invalid input!')
