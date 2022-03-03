import mathfuncs
#import pytest 

def test_add():
    assert mathfuncs.add(7, 3) == 10
    assert mathfuncs.add(7) == 9

def test_multiply():
    assert mathfuncs.multiply(7, 3) == 21
    assert mathfuncs.multiply(7, 2) == 14
