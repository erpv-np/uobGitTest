# test_hello.py
import pytest
from hello_world import hello_world

def test_hello():
    assert hello() == "Hello, World!"
