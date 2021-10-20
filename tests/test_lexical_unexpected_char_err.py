import pytest

from calculator.calculator import Lexer

@pytest.mark.parametrize('x,unexpected_char', [
  ('a', 'a'),
  ('ab', 'a'),
  ('1x', 'x'),
])
def test_lexer_catch_unexpected_char(x, unexpected_char):
  lex = Lexer(x)
  with pytest.raises(Exception) as e:
    lex.parse()

  assert f'unexpected character: {unexpected_char}' in str(e)
