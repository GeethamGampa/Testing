# Testing
Works on Testing Concept

## Unit Testing
Unit testing is a way to check if small parts of our code, called units (usually functions or methods), work correctly on their own.

We write special test programs that run these units with different inputs and compare the actual output with the expected output. If they match, the test passes; if not, it fails.

In Python, we often use the built-in unittest module to write and run these tests. Some common methods in unittest are:
```
assertEqual(a, b) — checks if a equals b

assertTrue(x) — checks if x is True

assertFalse(x) — checks if x is False

assertNotEqual(a, b) — checks if a is not equal to b

assertRaises(Exception) — checks if a specific error is raised
```

## PyTesting

Pytest is a popular testing tool in Python that helps us check if our small code parts (called units) work correctly by themselves.

We write test functions that call our code with different inputs and compare the actual results with what we expect. If the results match, the test passes; if not, it fails.

Pytest makes writing tests easy and clear. Here are some common ways to check conditions in pytest:
```
assert a == b — checks if a equals b

assert x — checks if x is True

assert not x — checks if x is False

assert a != b — checks if a is not equal to b

Use with pytest.raises(Exception): to check if a certain error is raised
```
Pytest automatically finds and runs all test functions in files named like test_*.py.




 
