import pytest

from calculator.calculator import Parser
from calculator.bootstrap import _mt

@pytest.mark.parametrize('x,expected_value', [
  (_mt('1 + 1'), 2),
  (_mt('1 - 1'), 0),
  (_mt('10 * 10'), 100),
  (_mt('200 / 2'), 100),
  (_mt('(100 + 100) * 2'), 400)
])
def test_parser_should_good(x, expected_value):
  r = Parser(x).parse()
  assert expected_value == r.eval()