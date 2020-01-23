# -*- coding: utf-8 -*-


def _squash(*args):
    """
    Unwraps ``IO`` values, merges them into tuple, and wrapps back.

    .. code:: python

        >>> from returns.io import IO, io_squash
        >>> str(io_squash(IO('a'), IO('b')))
        "<IO: ('a', 'b')>"

    """
    wrapper_class = type(args[0])
    return wrapper_class(tuple(
        container._inner_value  # noqa:  WPS437
        for container in args
    ))
