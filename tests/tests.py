from datetime import datetime
from unittest import TestCase, main
from pykeplib import TheCPower, Visual, Enigma, GetRandomData, SymbolRemove


class TestPyKepLib(TestCase, TheCPower, Visual, Enigma, GetRandomData, SymbolRemove):

    def test_get_json_logging(self):
        with self.assertRaises(FileNotFoundError) as ex:
            self.get_json_data('logging')
        self.assertEqual('File not found!', ex.exception.args[0])

    def test_get_json_product_details(self):
        with self.assertRaises(FileNotFoundError) as ex:
            self.get_json_data('product_details')
        self.assertEqual('File not found!', ex.exception.args[0])

    def test__get_cdll(self):
        with self.assertRaises(OSError) as ex:
            self._get_cdll()
        self.assertEqual('OS Error!', ex.exception.args[0])

    def test_get_date(self):
        self.assertEqual(self.get_date(), datetime.now().strftime('%d_%m_%Y'))

    def test__split_text(self):
        self.assertEqual(self._split_text('Python'), ['P', 'y', 't', 'h', 'o', 'n'])

    def test_get_coding_or_decoding_dict(self):
        self.assertEqual(type(self.get_coding_or_decoding_dict()), list)

    def test_get_system_command(self):
        self.assertEqual(self.get_system_command(), 'clear')  # 'cls' for windows

    def test_get_exponentiation(self):
        self.assertEqual(self.get_exponentiation(5), 25)

    def test_get_loading_points(self):
        self.assertEqual(self.get_loading_points('Загрузка', 3), 'Загрузка...')

    def test_coding(self):
        self.assertEqual(self.coding('Hello world!'), '222406695695474553948474635695399736')

    def test_decoding(self):
        self.assertEqual(self.decoding('222406695695474553948474635695399736'), 'Hello world!')

    def test_get_random_data(self):
        self.assertEqual(self.get_random_data(('λ',)), 'λ')

    def test_remove_symbols_return_word(self):
        self.assertEqual(
            self.remove_symbols_return_word(
                'удалено_Пример_удалено', '_', 2
            ), 'Пример'
        )

    def test_remove_symbols_from_sentence(self):
        self.assertEqual(
            self.remove_symbols_from_sentence(
                'Функционала_методов_', '_'
            ), 'Функционала методов '
        )


if __name__ == '__main__':
    main()