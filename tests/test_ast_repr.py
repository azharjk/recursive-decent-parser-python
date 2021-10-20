import pytest

from calculator.bootstrap import math_repr

@pytest.mark.parametrize('test_input,expected_repr', [
  ('1 + 1', '(1 + 1)'),
  ('1 - 1', '(1 - 1)'),
  ('1 * 1', '(1 * 1)'),
  ('1 / 1', '(1 / 1)'),
])
def test_ast_repr_should_good(test_input, expected_repr):
  assert expected_repr == math_repr(test_input)
