"""
Test Mathematics
~~~~~~~~~~~~~~~~

This module test functionality for the Mathematics module.
"""

from numbers import Number
from pathlib import Path

import tealogger

from pytest_sandbox.alpha.mathematics import Mathematics


CURRENT_MODULE_PATH = Path(__file__).parent.expanduser().resolve()

# Configure conftest_logger
tealogger.configure(
    configuration=CURRENT_MODULE_PATH.parents[1]
    / "configuration/sandbox.logger.json"
)
test_logger = tealogger.get_logger(__name__)


class TestMathematics:
    """Test Mathematics"""

    def test_add(
        self,
        first_number: Number,
        second_number: Number,
        expected: Number,
    ) -> None:
        """Test add method"""
        test_logger.info("Test Add")
        test_logger.debug(f"First Number: {first_number}")
        test_logger.debug(f"Second Number: {second_number}")
        test_logger.debug(f"Expected: {expected}")

        mathematics = Mathematics()

        assert mathematics.add(
            first_number=first_number,
            second_number=second_number
        ) == expected
