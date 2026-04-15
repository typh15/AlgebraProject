def natural_numbers(n):
    return tuple(range(n))


def symmetric_generators(n):
    """
    Adjacent transpositions generate S_n.
    Returns a list of functions.
    """
    generators = []

    for i in range(n - 1):
        def swap(x, i=i):
            if x == i:
                return i + 1
            if x == i + 1:
                return i
            return x

        generators.append(swap)

    return generators


def cyclic_generator(n):
    """
    A generator for the cyclic group C_n.
    """
    return lambda x: (x + 1) % n