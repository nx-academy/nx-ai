import sys
import os

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.utils.make_sum import make_sum


def test_make_sum():
    assert make_sum(2, 2) == 4
    assert make_sum(2, 2) != 6
    assert make_sum(0, 0) == 0 # Or la tête à toto
