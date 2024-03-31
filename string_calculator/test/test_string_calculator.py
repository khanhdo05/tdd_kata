import pytest
from src.string_calculator import *

# Step 1: A simple String calculator with the below method signature that takes in a string of up to two comma seperated numbers and returns the sum of those numbers.
# Delimiter: ,

def test_empty_string_gets_zero():
    assert StringCalculator.Add("") == 0

def test_3_gets_3():
    assert StringCalculator.Add("3") == 3

def test_11_5_gets_16():
    assert StringCalculator.Add("11,5") == 16

# Step 2: Allow the Add method to handle an unknown amount of numbers
# Delimiter: ,

def test_1_2_3_gets_6():
    assert StringCalculator.Add("1,2,3")

def test_larger_input_gets_correct_sum():
    assert StringCalculator.Add("1,2,3,9,3,4,2,4,3,3") == 34

# Step 3: Allow the Add method to handle new lines between numbers (instead of commas)
# Delimiter: , \n

def test_5_newline_11_gets_16():
    assert StringCalculator.Add("5\n11") == 16

def test_3_comma_17_newline_12_gets_32():
    assert StringCalculator.Add("3,17\n12") == 32
    
# Step 4: Support different delimiters
# Delimiter: , \n //[delimiter]\n[numbers…]

def test_3_c_11_gets_14():
    assert StringCalculator.Add("//c\n3c11") == 14

def test_3_semicolon_17_newline_12_comma_2():
    assert StringCalculator.Add("//;\n3;17\n12,2") == 34

# Step 5: Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. If there are multiple negatives, show all of them in the exception message.
# Delimiter: , \n //[delimiter]\n[numbers…]

def test_3_comma_negative_11_throws_exception_and_negative_11():
    with pytest.raises(ValueError) as excinfo:
        StringCalculator.Add("3,-11") 

    assert "negatives: -11 not allowed" in str(excinfo.value)

def test_negative_1_throws_exception_and_negative_1():
    with pytest.raises(ValueError) as excinfo:
        StringCalculator.Add("-1")
        
    assert "negatives: -1 not allowed" in str(excinfo.value)

def test_12_semicolon_negative_1_throws_exception_and_negative_1():
    with pytest.raises(ValueError) as excinfo:
        StringCalculator.Add("//;\n12;-1")
        
    assert "negatives: -1 not allowed" in str(excinfo.value)   