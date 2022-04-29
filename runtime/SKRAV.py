from ast import parse
import os, sys
from pyswip import Prolog
sys.path.insert(0, os.getcwd() + '/src/compiler')

from tokenizer import Tokenizer


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
    #parseTree = ''
    for soln in prolog.query("program(T, " + str(tokens) + ", [])"):
         parseTree = soln['T']
         #print(soln['T'])
    print(parseTree)
    # EVALUATE


