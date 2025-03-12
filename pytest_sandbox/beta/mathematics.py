"""
Mathematics
~~~~~~~~~~~

The module implements the core functionality of the Mathematics.
"""

from numbers import Number


class Mathematics:
    """Mathematics"""

    def __init__(
        self
    ) -> None:
        """Initialize Constructor

        Initialize the instance of the Mathematics class.
        """
        ...

    def add(
        self,
        first_number: Number,
        second_number: Number,
    ) -> Number:
        """Add

        Add the `first_number` with the `second_number`, and return the
        result.

        :param first_number: The first number to add
        :type first_number: Number
        :param second_number: The second number to add
        :type second_number: Number
        :return: The result of the addition
        :rtype: Number
        """
        return first_number + second_number

    def subtract(
        self,
        first_number: Number,
        second_number: Number,
    ) -> Number:
        """Subtract

        Subtract the `second_number` from the `first_number`, and return
        the result.

        :param first_number: The first number
        :type first_number: Number
        :param second_number: The second number
        :type second_number: Number
        :return: The result of the subtraction.
        :rtype: Number
        """
        return first_number - second_number
