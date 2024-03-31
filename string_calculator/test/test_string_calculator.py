import pytest
from src.string_calculator import *

# A simple String calculator with the below method signature that takes in a string of up to two comma seperated numbers and returns the sum of those numbers.

def test_empty_string_gets_zero():
    assert StringCalculator.Add("") == 0