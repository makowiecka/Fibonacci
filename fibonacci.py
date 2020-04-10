class Fibonacci:

    def __init__(self, n):
        self.n = n
        self.i = -1
        self.a = 0
        self.b = 1

    def __iter__(self):
        """Iterator."""
        return self

    def __next__(self):
        """Next."""
        fib = self.a
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        self.a, self.b = self.b, self.a + self.b

        return fib