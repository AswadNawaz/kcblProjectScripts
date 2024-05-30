import unittest

import pytest
import pandas as pd
import addition

def read_data_from_csv(path):
    """
    Read data from CSV file and return as a list of tuples.
    Assumes CSV file has headers.
    """
    data = pd.read_csv(path)
    return [tuple(x) for x in data.to_numpy()]

class TestAddition:
    @pytest.mark.parametrize("a, b, expected", read_data_from_csv("example.csv"))
    def test_add(self, a, b, expected):
        addd = addition.A()
        result = addd.add(a, b)
        assert result == expected

