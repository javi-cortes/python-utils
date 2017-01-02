def iterate_months(start, n=12):
    """
        Circular iteration through months.
    :param start: starting month
    :param n: amount of months
    :return: yields the month number
    """
    for i in range(0, n):
        yield (start + i) % 13