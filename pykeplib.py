from ctypes import *
from random import choice
from platform import system
from ast import literal_eval
from accessify import protected


class CKepLib:
    @protected
    @staticmethod
    def _get_cdll():
        return CDLL("./ckeplib.so")


class PyKepLib:
    @protected
    @staticmethod
    def _split_text(text):
        return [i for i in text]

    @protected
    @staticmethod
    def _get_coding_or_decoding_dict(dict_file):
        with open(str(dict_file)) as cd:
            coding_or_decoding_dict = literal_eval(cd.read())
        return coding_or_decoding_dict


class TheCPower(CKepLib):
    def get_exponentiation(self, value):
        return self._get_cdll().main(value)


class System(PyKepLib):
    @staticmethod
    def get_system_command() -> str:
        """
        Метод возвращает команды для текущей ос
        :return: str
        """
        system_name = system()
        if system_name == 'Linux':
            return 'clear'
        elif system_name == 'Windows':
            return 'cls'


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
        if int(counter) == 1:
            return f'{download_text}'
        elif int(counter) == 2:
            return f'{download_text}.'
        elif int(counter) == 3:
            return f'{download_text}..'
        elif int(counter) == 4:
            return f'{download_text}...'


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
                transfer_first.append(self._get_coding_or_decoding_dict('coding_dict_first.spec')[i])
            for i in self._split_text(''.join(transfer_first)):
                transfer_second.append(self._get_coding_or_decoding_dict('coding_dict_second.spec')[i])

            return ''.join(transfer_second)

        except KeyError:
            return "Ошибка кодирования!"

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
                transfer_second.append(self._get_coding_or_decoding_dict('decoding_dict_first.spec')[i])
            for i in transfer_second:
                transfer_third.append(self._get_coding_or_decoding_dict('decoding_dict_second.spec')[i])

            return ''.join(transfer_third)

        except KeyError:
            return "Ошибка кодирования!"


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
    @staticmethod
    def remove_symbols_return_word(word_with_symbol, removed_symbol, word_number) -> str:
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
            return "Неверный ввод!"

    @staticmethod
    def remove_symbols_from_sentence(suggestion, removed_symbol) -> str:
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
            return "Неверный ввод!"
