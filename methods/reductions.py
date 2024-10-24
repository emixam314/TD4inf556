from data_classes.boundary_matrix import BoundaryMatrix

class Reduction:
    def __init__(self, B:BoundaryMatrix):
        self.B = B
        self.n = len(B.B)

    def low_pivot(self, j):
        """Returns the row index of the lowest 1 in column j, or None if the column is empty."""
        if self.B.B[j]:
            return max(self.B.B[j]) 
        return None

    def add_columns(self, j, i):
        """Adds column i to column j (B[j] = B[j] + B[i]) in Z2."""
        self.B.B[j] ^= self.B.B[i]  

    def reduce_boundary_matrix(self):
        """Reduces the sparse boundary matrix B using column operations in Z2."""
        pass
        

class Naive_reduction(Reduction):

    def reduce_boundary_matrix(self):
        """Reduces the sparse boundary matrix B using column operations in Z2."""
        for j in range(self.n):
            for l in range(j):
                pivot = self.low_pivot(j)
                l_pivot = self.low_pivot(l)
                if pivot is not None and pivot == l_pivot: 
                    self.add_columns(j, l)
        return self.B
    
class Optimal_reduction(Reduction):

    def __init__(self, B: BoundaryMatrix):
        super().__init__(B)
        self.pivot_columns = {}

    def reduce_boundary_matrix(self):
        """Reduces the sparse boundary matrix B using column operations in Z2."""
        for j in range(self.n):
            while True:
                pivot = self.low_pivot(j)
                if pivot is None: 
                    break
                if pivot in self.pivot_columns:
                    self.add_columns(j, self.pivot_columns[pivot])
                else:
                    self.pivot_columns[pivot] = j
                    break

        return self.B