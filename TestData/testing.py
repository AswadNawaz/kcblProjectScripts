import pytest

def add(a, b):
    return a + b

class TestAddition:
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),   # Test case 1
        (0, 0, 0),   # Test case 2
        (-1, 1, 0),  # Test case 3
        (2, -2, 0)   # Test case 4
    ])
    def test_add(self, a, b, expected):
        result = add(a, b)
        assert result == expected