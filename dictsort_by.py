def dictsort_by(d, order, items=False, skip=True):
    """
        Iterate a dict in order. If k from order not found in d yield rest of d elements.
    :param d: dict to iterate.
    :param order: List with the keys order.
    :param items: flag to return k or (k, v)
    :param skip: only returns d.keys() & order and skips the rest.
    :return: yields each element of the dict in order if possible.
    """
    _d = d.copy()
    while _d:
        for ko in order:
            if ko in _d:
                v = _d.pop(ko)
                yield ko if not items else (ko, v)
        if not skip:
            # return the rest of the dict
            yield _d.popitem()[0] if not items else _d.popitem()
        else:
            return