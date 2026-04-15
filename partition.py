
class Partition:
    def __init__(self, values):
        if isinstance(values, int):
            self.values = [values]
        else:
            self.values = sorted(values, reverse=True)

    def clean(self):
        """Remove zero entries."""
        self.values = [v for v in self.values if v != 0]

    def transpose(self):
        """Return conjugate partition."""
        result = []
        temp = self.values.copy()

        for _ in range(max(self.values)):
            count = sum(1 for v in temp if v > 0)
            temp = [v - 1 for v in temp]
            result.append(count)

        return Partition(result)

    def __add__(self, other):
        length = max(len(self.values), len(other.values))
        result = []

        for i in range(length):
            a = self.values[i] if i < len(self.values) else 0
            b = other.values[i] if i < len(other.values) else 0
            result.append(a + b)

        return Partition(result)

    def __repr__(self):
        return f"Partition({self.values})"