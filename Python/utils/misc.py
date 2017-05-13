"""
Miscellaneous utilities used by Python algorithms code.
"""


def swap(l, i, j):
    """
    Since several sort algorithms need to swap list
    elements, we provide a swap function.

    Args:
        l: the list
        i, j: the indices of the elements to swap.
    """
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
