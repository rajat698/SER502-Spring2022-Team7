from ast import parse
import os, sys
from pyswip import Prolog
sys.path.insert(0, os.getcwd() + '/src/compiler')

from tokenizer import Tokenizer
from evaluator import Evaluator


if __name__=='__main__':
    #READ FILE
    file = open("src/test.txt", "r")
    program =  file.read()
    # TOKENIZE
    Tk = Tokenizer()
    tokens = Tk.tokenizeProgram(program)
    #print(tokens)
    # PARSE
    prolog = Prolog()
    prolog.consult('src/compiler/parser.pl')
    query = "program(T, " + str(tokens) + ", [])."
    #print(query)
    #parseTree = ''
    for soln in prolog.query(query):
         parseTree = soln['T']
         break
         #print(soln['T'])
    #print(parseTree)
    # EVALUATE
    eval = Evaluator()
    eval.evaluate(parseTree)
    print('PROGRAM TERMINATED')
    print('ENV: ', eval.env)
    


