import pytest

from calculator.bootstrap import math_eval

@pytest.mark.parametrize('test_input,expected', [
  ('100 + 100', 200),
  ('90 - 2', 88),
  ('1 * 100', 100),
  ('8 / 2', 4),
])
def test_simple(test_input, expected):
  assert math_eval(test_input) == expected
