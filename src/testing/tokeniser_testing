import unittest
from unittest import result
import sys

sys.path.insert(0, '../SER502-Spring2022-Team7/src')
from SCRAV_tokeniser import tokenise


class Testing(unittest.TestCase):
    testCase_1 = "str x4;\nbool ay23 = False;\nint zz111z = 2 + 3 * 5;\nx = \"abc\";"
    expected_1 = ['str', 'x4', ';', 'bool', 'ay23', '=', 'False', ';', 'int', 'zz111z', '=', '2', '+', '3', '*', '5', ';', 'x', '=', '"', 'abc', '"', ';']

    testCase_2 = "y = not y;\nbool z = True or False;"
    expected_2 = ['y', '=', 'not', 'y', ';', 'bool', 'z', '=', 'True', 'or', 'False', ';']

    
    def test1(self):
        result = tokenise(Testing.testCase_1)
        self.assertEqual(result, Testing.expected_1)
    
    def test2(self):
        result = tokenise(Testing.testCase_2)
        self.assertEqual(result, Testing.expected_2)

if __name__ == '__main__':
    unittest.main()