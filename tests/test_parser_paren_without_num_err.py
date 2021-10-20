import pytest

from calculator.bootstrap import _mt
from calculator.calculator import Parser

@pytest.mark.parametrize('x', [
  ('()'),
  ('(())'),
  ('()('),
])
def test_parser_without_number_err(x):
  with pytest.raises(Exception) as e:
    Parser(_mt(x)).parse()

  assert 'creating tree failed maybe you does not provide any number' in str(e)