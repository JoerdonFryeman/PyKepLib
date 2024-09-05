from unittest import TestCase, main
from pykeplib import SQLite, TheCPower, Visual, Enigma, DataProcessing, TextWork, FileHandling


class TestPyKepLib(TestCase, TheCPower, Visual, Enigma, DataProcessing, TextWork, FileHandling):
    def test_get_json_data(self):
        try:
            self.get_json_data('logging')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_db_from_config(self):
        self.assertEqual(self.get_db_from_config(), SQLite)

    def test_select_os_command(self):
        self.assertEqual(self.select_os_command('library_format'), '.so')  # 'dll' for windows

    def test_get_cdll(self):
        try:
            self.get_cdll()
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_coding_dict_zero(self):
        try:
            self.get_json_data('coding_or_decoding_dict/coding_dict_zero')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_coding_dict_one(self):
        try:
            self.get_json_data('coding_or_decoding_dict/coding_dict_one')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_decoding_dict_two(self):
        try:
            self.get_json_data('coding_or_decoding_dict/decoding_dict_two')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_decoding_dict_three(self):
        try:
            self.get_json_data('coding_or_decoding_dict/decoding_dict_three')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')

    def test_get_exponentiation(self):
        self.assertEqual(self.get_exponentiation(5), 25)

    def test_get_exponentiation_decorator(self):
        self.assertEqual(self.get_exponentiation(5), 25)

    def test_get_loading_points(self):
        self.assertEqual(self.get_loading_points('Loading', 3), 'Loading...')

    def test_wake_up_neo(self):
        self.assertEqual(self.wake_up_neo(['The test', 'is', 'working!']), None)

    def test_coding(self):
        self.assertEqual(self.coding('Hello world!'), '222406695695474553948474635695399736')

    def test_decoding(self):
        self.assertEqual(self.decoding('222406695695474553948474635695399736'), 'Hello world!')

    def test_get_random_data(self):
        random_data = self.get_random_data()
        self.assertEqual(random_data(('λ',)), 'λ')

    def test_remove_symbols_return_word(self):
        self.assertEqual(
            self.remove_symbols_return_word(
                'deleted_Example_deleted', '_', 2
            ), 'Example'
        )

    def test_remove_symbols_from_sentence(self):
        self.assertEqual(
            self.remove_symbols_from_sentence(
                'Functional_of_the_method', '_'
            ), 'Functional of the method'
        )

    def test_make_and_get_script_hidden_in_file(self):
        try:
            self.make_script_hidden_in_file('pykeplib', 'png', 'pykeplib', 'py')
            try:
                self.get_script_hidden_in_file('pykeplib_copy', 'png', 'pykeplib_copy', 'py', '60 82')
            except Exception as e:
                self.fail(f'Function raised an exception {e}')
        except Exception as e:
            self.fail(f'Function raised an exception {e}')


if __name__ == '__main__':
    main()
