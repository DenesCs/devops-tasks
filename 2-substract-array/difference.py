#!/usr/bin/env python3
# Description: Difference function
# Author: Denes Csizmadia
# Date: 02-12-2021

import sys
import argparse
import logging
from logging import critical, error, info, warning, debug

def array_diff(list_a,list_b):
    return [x for x in list_a if x not in list_b]

def test_array_diff(list_a,list_b,expected):
    assert array_diff(list_a,list_b) == expected, str(list_a) + " - " + str(list_b) + " should be " + str(expected) 

def main():
    test_array_diff([1,2],[1],[2])
    test_array_diff([1,2,2],[1],[2,2])
    test_array_diff([1,2,2],[2],[1])
    test_array_diff([1,2,2],[],[1,2,2])
    test_array_diff([],[1,2],[])
    test_array_diff([1,2,3],[1,2],[3])
    print("Tests passed")

if __name__ == '__main__':
    main()
