import pytest
from powFuncs import pow1, pow2, pow3 

def test_method_pow1():
    assert pow1(2, 2) == 4
    assert pow1(0, 2) == 0
    assert pow1(2, 1) == 2
    assert pow1(10, 2) == 100
    assert pow1(2, 0) == 1

def test_method_pow2():
    assert pow2(2, 2) == 4
    assert pow2(0, 2) == 0
    assert pow2(2, 1) == 2
    assert pow2(10, 2) == 10
    assert pow2(2, 0) == 1

def test_method_pow3():
    assert pow3(2, 2) == 4
    assert pow3(0, 2) == 0
    assert pow3(2, 1) == 2
    assert pow3(10, 2) == 100
    assert pow3(2, 0) == 1
 