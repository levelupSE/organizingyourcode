import unittest
from unittest.mock import Mock
from todo_v3 import run, todos_to_csv

class TestTodo(unittest.TestCase):

    def test_run(self):
        filename = 'test.csv'
        user_inputs = [('a', 1), ('b', 2)]
        csv_contents = 'contents'
        todos_to_csv = Mock(return_value=csv_contents)
        write_rows = Mock()

        run(filename, user_inputs, todos_to_csv, write_rows)

        todos_to_csv.assert_called_with(user_inputs)
        write_rows.assert_called_with(filename, csv_contents)

    def test_todos_to_csv(self):
        user_inputs = [('a', 1), ('b', 2)]
        expected_contents = 'a,1\nb,2\n'

        contents = todos_to_csv(user_inputs)
        self.assertEqual(contents, expected_contents)


if __name__ == '__main__':
    unittest.main()
