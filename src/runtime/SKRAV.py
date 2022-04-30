from ast import parse
import os, sys
from pyswip import Prolog

# os.system("pip3 install requests")
sys.path.insert(0, os.getcwd() + '/src/compiler')

from tokenizer import Tokenizer
from evaluator import Evaluator

if __name__=='__main__':
     #READ FILE
     file = open("data/new.xxx", "r")
     program =  file.read()
     # TOKENIZE
     Tk = Tokenizer()
     tokens = Tk.tokenizeProgram(program)
     #print(tokens)
     # PARSE
     prolog = Prolog()
     prolog.consult('src/compiler/parser.pl') 
     query = "program(T, " + str(tokens) + ", [])."
     # print(query)
     #parseTree = ''
     for soln in prolog.query(query):
          parseTree = soln['T']
          break
     #print(parseTree)
     #exit()

     # EVALUATE
     eval = Evaluator()
     eval.evaluate(parseTree)
     print('PROGRAM EXECUTED')
     print('ENV: ', eval.env)
     print('FN: ', eval.functions)
    


