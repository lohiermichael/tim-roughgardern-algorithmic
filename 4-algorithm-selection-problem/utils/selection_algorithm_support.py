def check_order_statistics(L: list, i: int) -> None:
    """
    Raise an error if the number of order statistic is not in [0..len(L)-1]
    Args:
        L (list): Input list of integers
        i (int): number of order statistic of the input list in [0..len(L)-1]

    Returns:
        None
    """
    if 0 <= i <= len(L) - 1:
        pass
    else:
        raise ValueError(
            "The number of order statistic is out of range. Please choose it in [0..len(L)-1]"
        )
