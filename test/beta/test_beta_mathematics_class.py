"""
Test Beta Mathematics Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module test functionality of the Mathematics module on a class
level.
"""

from numbers import Number
from pathlib import Path

import pytest
import tealogger

from pytest_sandbox.beta.mathematics import Mathematics

CURRENT_MODULE_PATH = Path(__file__).parent.expanduser().resolve()

# Configure conftest_logger
tealogger.configure(
    configuration=CURRENT_MODULE_PATH.parents[1] / "configuration/sandbox.logger.json"
)
test_logger = tealogger.get_logger(__name__)


@pytest.mark.beta
class TestBetaMathematicsClass:
    """Test Mathematics"""

    def test_add(
        self,
        first_number: Number,
        second_number: Number,
        expected: Number,
    ) -> None:
        """Test add method

        :param first_number: The first number to add
        :type first_number: Number
        :param second_number: The second number to add
        :type second_number: Number
        :param expected: The expected result of the addition
        :type expected: Number
        """
        test_logger.info("Test Add")
        test_logger.debug(f"First Number: {first_number}")
        test_logger.debug(f"Second Number: {second_number}")
        test_logger.debug(f"Expected: {expected}")

        mathematics = Mathematics()

        assert (
            mathematics.add(first_number=first_number, second_number=second_number)
            == expected
        )

    def test_subtract(
        self,
        first_number: Number,
        second_number: Number,
        expected: Number,
    ) -> None:
        """Test subtract method

        :param first_number: The first number
        :type first_number: Number
        :param second_number: The second number
        :type second_number: Number
        :param expected: The expected result of the subtraction
        :type expected: Number
        """
        test_logger.info("Test Subtract")
        test_logger.debug(f"First Number: {first_number}")
        test_logger.debug(f"Second Number: {second_number}")
        test_logger.debug(f"Expected: {expected}")

        mathematics = Mathematics()

        assert (
            mathematics.subtract(first_number=first_number, second_number=second_number)
            == expected
        )
