from app import index
from flask import Flask

def test_index():
    assert index() == "Hello World!"