from .calculator import Lexer, Parser

def _mt(x):
  return Lexer(x).parse()

def math_eval(x):
  return Parser(Lexer(x).parse()).parse().eval()

def math_repr(x):
  return Parser(Lexer(x).parse()).parse().s()
