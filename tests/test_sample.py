# -*- coding: utf-8 -*-
""" pytest
"""
from modules import sample


def test_get_name():
    """ Test sample get_name
    """
    assert sample.get_name('foo') == 'foo'
    assert sample.get_name('foo', 'bar') == 'barfoo'
    assert sample.get_name('foo', 'bar', 'postfix') == 'barfoopostfix'

def test_get_bool():
    """ Test sample get_bool
    """
    assert sample.get_bool() == True
    assert sample.get_bool(True) == True
