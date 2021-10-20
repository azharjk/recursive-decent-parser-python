from calculator.bootstrap import _mt
from calculator.calculator import Parser

def main():
  print(Parser(_mt('(10000 + 100000) - 12 * 7 / 12')).parse().eval())

if __name__ == '__main__':
  main()
