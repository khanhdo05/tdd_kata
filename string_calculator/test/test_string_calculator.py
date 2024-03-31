import pytest
from src.string_calculator import *

# Batch 1: A simple String calculator with the below method signature that takes in a string of up to two comma seperated numbers and returns the sum of those numbers.
# Delimiter: ,

def test_empty_string_gets_zero():
    assert StringCalculator.Add("") == 0

def test_3_gets_3():
    assert StringCalculator.Add("3") == 3

def test_11_5_gets_16():
    assert StringCalculator.Add("11,5") == 16

# Batch 2: Allow the Add method to handle an unknown amount of numbers
# Delimiter: ,

def test_1_2_3_gets_6():
    assert StringCalculator.Add("1,2,3")

def test_larger_input_gets_correct_sum():
    assert StringCalculator.Add("1,2,3,9,3,4,2,4,3,3") == 34