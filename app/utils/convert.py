from decimal import Decimal


def calculate_fx(current: Decimal, rate: Decimal) -> Decimal:
    """calculates exchange rate

    :param current: current value
    :type current: float
    :param rate: current exchange rate
    :type rate: float
    :return: new value
    :rtype: float
    """

    return current * rate
