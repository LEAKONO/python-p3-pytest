#!/usr/bin/env python3


# lib/testing/test_not_none.py
from not_none_functions import return_not_none

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" should return a non-None value.'''
    assert return_not_none() is not None

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
