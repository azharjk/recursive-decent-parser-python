import pytest

from calculator.calculator import Parser
from calculator.bootstrap import _mt

@pytest.mark.parametrize('x,expected', [
  (_mt('((10 + 2) * 2) + 1'), 25),
])
def test_parser_should_handle_nested_paren(x, expected):
  assert expected == Parser(x).parse().eval()