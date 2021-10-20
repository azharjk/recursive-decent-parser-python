import pytest

from calculator.calculator import Lexer

@pytest.mark.parametrize('test_input,expected_size', [
  ('100', 2),
  ('*/+-', 5),
  ('1+2*/', 6),
  ('100', 2),
  ('()', 3),
  ('(())', 5),
  ('1(12())', 7),
  ('23(2+2)', 7),
])
def test_lexer_behave_good(test_input, expected_size):
  tokens = Lexer(test_input).parse()
  assert len(tokens) == expected_size