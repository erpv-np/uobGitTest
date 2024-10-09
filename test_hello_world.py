# test_hello.py
import pytest
from hello import hello

def test_hello():
    assert hello() == "Hello, World!"
