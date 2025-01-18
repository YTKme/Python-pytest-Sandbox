"""
Test Mathematics
~~~~~~~~~~~~~~~~

This module test functionality for the Mathematics module.
"""

from pytest_sandbox.alpha.mathematics import Mathematics

class TestMathematics:
    """Test Mathematics"""

    def test_add(
        self
    ) -> None:
        """Test add method"""
        mathematics = Mathematics()

        assert mathematics.add(1, 2) == 3
        assert mathematics.add(-1, 1) == 0

