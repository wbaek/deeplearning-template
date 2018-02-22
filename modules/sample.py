# -*- coding: utf-8 -*-
"""Example Sample docstrings.

This module sample documentation as specified by the python style guide
"""


def get_name(name, prefix='', postfix=''):
    """Example funciton with types documented in the docstring.

    Args:
        name (str): name stsring
        prefix (str): prefix string
        postfix (Str): postfix string

    Returns:
        str: return value prefix+name+postfix
    """

    return prefix+name+postfix


def get_bool(true_or_false=True):
    """converage test sample
    """
    if true_or_false:
        return True
    else:
        return False
