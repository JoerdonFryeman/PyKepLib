import csv
import json
from ctypes import *
from random import choice
from platform import system
from datetime import datetime
from logging import config, getLogger


class Descriptor:
    def __set_name__(self, owner, name) -> None:
        self.name = f"_{name}"

    def __get__(self, instance, owner) -> int:
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Base:
    @staticmethod
    def get_json_data(name) -> dict:
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
    def get_date():
        date = datetime.now().strftime('%d_%m_%Y')
        return date

    @staticmethod
    def _split_text(text):
        return [i for i in text]

    def __create_coding_or_decoding_dict(self):
        coding_or_decoding_dict = [
            self.get_json_data('coding_or_decoding_dict/coding_dict_zero'),
            self.get_json_data('coding_or_decoding_dict/coding_dict_one'),
            self.get_json_data('coding_or_decoding_dict/decoding_dict_two'),
            self.get_json_data('coding_or_decoding_dict/decoding_dict_three')
        ]
        return coding_or_decoding_dict

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


class Visual(PyKepLib):
    @staticmethod
    def get_loading_points(download_text, counter) -> str:
        """
        Метод принимает значение счётчика и возвращает при
        различных его значениях разное колличество точек.

        :param download_text: str
        :param counter: int
        :return: str
        """
        dictionary = {
            '0': lambda x: download_text,
            '1': lambda x: download_text + '.',
            '2': lambda x: download_text + '..',
            '3': lambda x: download_text + '...',
        }[str(counter)](download_text)
        return dictionary


class Enigma(PyKepLib):
    def coding(self, text) -> str:
        """
        Метод принимает строковую или числовую информацию и
        возвращает её в кодированном строковом виде.

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
            self.logger.error('Ошибка кодирования!')

    def decoding(self, code) -> str:
        """
        Метод принимает строковый или числовой код и
        возвращает информацию в декодированном строковом виде.

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
            self.logger.error('Ошибка кодирования!')


class GetRandomData(PyKepLib):
    transfer_list = []

    def get_random_data(self, data_list) -> str:
        """
        Метод принимает список или кортеж объектов, с помощью цикла добавляет их в список transfer_list
        класса GetRandomData и не повторяясь возвращает в случайном порядке.

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
    def remove_symbols_return_word(self, word_with_symbol, removed_symbol, word_number) -> str:
        """
        Метод убирает из слова или предложения принимаемый в строковом виде символ и
        возвращает выбранное третьим параметром в виде числа слово.

        :param word_with_symbol: str
        :param removed_symbol: str
        :param word_number: int
        :return: str
        """
        try:
            return (''.join(word_with_symbol)).split(removed_symbol)[word_number - 1]
        except (TypeError, IndexError, ValueError):
            self.logger.error('Неверный ввод!')

    def remove_symbols_from_sentence(self, suggestion, removed_symbol) -> str:
        """
        Метод убирает из слова или предложения принимаемый в виде строки
        вторым параметром символ и возвращает это слово или предложение.

        :param suggestion: str
        :param removed_symbol: str
        :return: str
        """
        try:
            return ' '.join(suggestion.split(removed_symbol))
        except (TypeError, AttributeError, ValueError):
            self.logger.error('Неверный ввод!')
