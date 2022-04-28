import unittest
from unittest import result
import sys

sys.path.insert(0, "/Users/abhishek/Assignments/Spring'22/SER502/Project/SER502-Spring2022-Team7/src")
from SCRAV_tokeniser import tokenise


class Testing(unittest.TestCase):
    testCase_1 = "str x4;\nbool ay23 = False;\nint zz111z = 2 + 3 * 5;\nx = \"abc\";"
    expected_1 = ['str', 'x4', ';', 'bool', 'ay23', '=', 'False', ';', 'int', 'zz111z', '=', '2', '+', '3', '*', '5', ';', 'x', '=', '"', 'abc', '"', ';']

    testCase_2 = "y = not y;\nbool z = True or False;"
    expected_2 = ['y', '=', 'not', 'y', ';', 'bool', 'z', '=', 'True', 'or', 'False', ';']

    testCase_3 = "int a = x+y/4;"
    expected_3 = ['int', 'a', '=', 'x', '+', 'y' ,'/', '4', ';']

    testCase_4 = "shuru\n int x;\n str zzz;"
    expected_4 = ['shuru', 'int', 'x', ';','str', 'zzz', ';']

    testCase_5 = '''shuru\n int x;\n str zzz ="Hello World";\n for-loop (i=10;i<10;i++;) \n { \n display '''
    expected_5 = ['shuru', 'int', 'x', ';', 'str', 'zzz', '=', '“Hello', 'world”', ';', 'for-loop', '(', 'i', '=', '1', ';', 'i', '<', '10', ';', 'i', '=', 'i', '+', '1', ';', ')', '{', 'display']

    testCase_6 = '''display "Something" '''
    expected_6 = ['display', '"', 'Something', '"']
    
    def test1(self):
        result = tokenise(Testing.testCase_1)
        self.assertEqual(result, Testing.expected_1)
    
    def test2(self):
        result = tokenise(Testing.testCase_2)
        self.assertEqual(result, Testing.expected_2)

    def test3(self):
        result = tokenise(Testing.testCase_3)
        self.assertEqual(result, Testing.expected_3)
    
    def test4(self):
        result = tokenise(Testing.testCase_4)
        self. assertEqual(result, Testing.expected_4)

    def test5(self):
        result = tokenise(Testing.testCase_5)
        self.assertEqual(result, Testing.expected_5)

    def test6(self):
        result = tokenise(Testing.testCase_6)
        self.assertAlmostEqual(result, Testing.expected_6)

if __name__ == '__main__':
    unittest.main()