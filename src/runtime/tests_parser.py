from ast import parse
import os, sys
from pyswip import Prolog
sys.path.insert(0, '/Users/abhishek/Assignments/Spring-22/SER502/Project/SER502-Spring2022-Team7/src/compiler')

from tokenizer import Tokenizer
from evaluator import Evaluator

def testcase(file_path):
    file = open(file_path, "r")
    program =  file.read()
    # TOKENIZE
    Tk = Tokenizer()
    tokens = Tk.tokenizeProgram(program)
    #print(tokens)
    # PARSE
    prolog = Prolog()
    prolog.consult('/Users/abhishek/Assignments/Spring-22/SER502/Project/SER502-Spring2022-Team7/src/compiler/parser.pl')
    query = "program(T, " + str(tokens) + ", [])."
    #print(query)
    parseTree = ''
    for soln in prolog.query(query):
            parseTree = soln['T']
    print(parseTree)
    eval = Evaluator()
    eval.evaluate(parseTree)

testcase("/Users/abhishek/Assignments/Spring-22/SER502/Project/SER502-Spring2022-Team7/src/test1.txt")
testcase("/Users/abhishek/Assignments/Spring-22/SER502/Project/SER502-Spring2022-Team7/src/test2.txt")
