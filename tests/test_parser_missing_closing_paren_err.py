import pytest

from calculator.calculator import Parser
from calculator.bootstrap import _mt

@pytest.mark.parametrize('x', [
  ('(10'),
  ('((10)'),
  ('((232)+10'),
  ('232+((10)')
])
def test_parser_should_catch_missing_paren(x):
  p = Parser(_mt(x))
  with pytest.raises(Exception) as e:
    p.parse()

  assert 'missing closing parenthesis' in str(e)
