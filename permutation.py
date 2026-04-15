class Permutation:
    """
    Represents a permutation of a finite domain.
    """

    def __init__(self, mapping, domain):
        self.domain = tuple(sorted(domain))
        self.image_tuple = tuple(mapping(x) for x in self.domain)

    def apply(self, x):
        return self.image_tuple[x - min(self.domain)]

    def __mul__(self, other):
        """
        Composition: self ∘ other
        """
        if self.domain != other.domain:
            raise ValueError("Permutations must have the same domain.")
        return Permutation(lambda x: self.apply(other.apply(x)), self.domain)

    def inverse(self):
        """
        Return the inverse permutation.
        """
        inverse_map = {
            self.image_tuple[i]: self.domain[i]
            for i in range(len(self.domain))
        }
        return Permutation(lambda x: inverse_map[x], self.domain)

    def conjugate_by(self, other):
        """
        Conjugate this permutation by another:
        other^{-1} * self * other
        """
        return other.inverse() * self * other

    def cycle_decomposition(self):
        """
        Return the permutation as a list of disjoint cycles.
        Fixed points are omitted.

        Example:
            (0, 2, 1) -> [(1, 2)]
            (1, 2, 0) -> [(0, 1, 2)]
        """
        visited = set()
        cycles = []

        for start in self.domain:
            if start in visited:
                continue

            current = start
            cycle = []

            while current not in visited:
                visited.add(current)
                cycle.append(current)
                current = self.apply(current)

            if len(cycle) > 1:
                cycles.append(tuple(cycle))

        return cycles

    def cycle_type(self):
        """
        Return the partition corresponding to the cycle lengths.
        Fixed points are included.

        Example:
            identity on 3 elements -> (1, 1, 1)
            (0, 2, 1) -> (2, 1)
            (1, 2, 0) -> (3)
        """
        visited = set()
        lengths = []

        for start in self.domain:
            if start in visited:
                continue

            current = start
            length = 0

            while current not in visited:
                visited.add(current)
                current = self.apply(current)
                length += 1

            lengths.append(length)

        return tuple(sorted(lengths, reverse=True))

    def __eq__(self, other):
        return isinstance(other, Permutation) and self.image_tuple == other.image_tuple

    def __hash__(self):
        return hash(self.image_tuple)

    def __repr__(self):
        return f"Permutation({self.image_tuple})"

    def __pow__(self, other):
        """
        If other is a permutation, perform conjugation.
        """
        if isinstance(other, Permutation):
            return other.inverse() * self * other
        raise TypeError("Exponent must be a Permutation for conjugation.")