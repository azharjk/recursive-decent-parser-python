from enum import Enum, auto

class TokenType(Enum):
  NUMBER   = auto()
  PLUS     = auto()
  MINUS    = auto()
  ASTERISK = auto()
  SLASH    = auto()
  LPAREN   = auto()
  RPAREN   = auto()
  EOS      = auto()

class Token:
  def __init__(self, t_type, value):
    self.t_type = t_type
    self.value = value

class Number:
  def __init__(self, data):
    self.data = data

  def eval(self):
    return self.data

  def s(self):
    return self.data

class Operator:
  def __init__(self, left, right):
    self.left = left
    self.right = right

class Addition(Operator):
  def eval(self):
    return self.left.eval() + self.right.eval()

  def s(self):
    return f'({self.left.s()} + {self.right.s()})'

class Subtraction(Operator):
  def eval(self):
    return self.left.eval() - self.right.eval()

  def s(self):
    return f'({self.left.s()} - {self.right.s()})'

class Multiplication(Operator):
  def eval(self):
    return self.left.eval() * self.right.eval()

  def s(self):
    return f'({self.left.s()} * {self.right.s()})'

class Division(Operator):
  def eval(self):
    return self.left.eval() / self.right.eval()

  def s(self):
    return f'({self.left.s()} / {self.right.s()})'

class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.size   = len(tokens)
    self.cursor = 0
    self.paren  = 0
    self.result_tree = None

  def expr(self):
    a = self.term()
    while True:
      if self.peek().t_type == TokenType.PLUS:
        self.next()
        b = self.term()
        a = Addition(a, b)
      elif self.peek().t_type == TokenType.MINUS:
        self.next()
        b = self.term()
        a = Subtraction(a, b)
      else:
        return a

  def term(self):
    a = self.factor()
    while True:
      if self.peek().t_type == TokenType.ASTERISK:
        self.next()
        b = self.factor()
        a = Multiplication(a, b)
      elif self.peek().t_type == TokenType.SLASH:
        self.next()
        b = self.factor()
        a = Division(a, b)
      else:
        return a

  def factor(self):
    if self.peek().t_type == TokenType.NUMBER:
      a = Number(self.peek().value)
      self.next()
      return a
    elif self.peek().t_type == TokenType.LPAREN:
      self.next()
      a = self.expr()
      if self.peek().t_type == TokenType.RPAREN:
        self.next()
        return a
      else:
        raise Exception('missing closing parenthesis')
    elif self.peek().t_type == TokenType.EOS:
      pass

  def parse(self):
    self.result_tree = self.expr()
    if self.result_tree is None:
      raise Exception('creating tree failed maybe you does not provide any number')
    return self.result_tree

  def peek(self):
    return self.tokens[self.cursor]

  def next(self):
    if self.cursor < self.size - 1:
      self.cursor += 1

class Lexer:
  def __init__(self, s):
    self.s        = s
    self.tokens   = []
    self.temp_str = ''

  def parse(self):
    for c in self.s:
      if c.isdigit():
        self.temp_str += c
      elif c == ' ':
        pass
      elif c == '(':
        self.add_number_token() 
        self.tokens.append(Token(TokenType.LPAREN, 0))
      elif c == ')':
        self.add_number_token() 
        self.tokens.append(Token(TokenType.RPAREN, 0))
      elif c == '+':
        self.add_number_token() 
        self.tokens.append(Token(TokenType.PLUS, 0))
      elif c == '-':
        self.add_number_token()
        self.tokens.append(Token(TokenType.MINUS, 0))
      elif c == '*':
        self.add_number_token()
        self.tokens.append(Token(TokenType.ASTERISK, 0))
      elif c == '/':
        self.add_number_token()
        self.tokens.append(Token(TokenType.SLASH, 0))
      else:
        raise Exception(f'unexpected character: {c}')
      
    self.add_number_token()
    self.tokens.append(Token(TokenType.EOS, 0))

    return self.tokens

  def add_number_token(self):
    if len(self.temp_str) > 0:
      self.tokens.append(Token(TokenType.NUMBER, int(self.temp_str)))
      self.temp_str = ''
