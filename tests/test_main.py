

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import foo


def test_foo_0():
    assert foo(3) > 5

def test_foo_1():
    assert foo(4) == 10
