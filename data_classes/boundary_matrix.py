from data_classes.filtration import Filtration
from data_classes.simplex import Simplex

class BoundaryMatrix:

    def __init__(self, B):
        self.B = B

    @staticmethod
    def build_sparse_boundary_matrix(filtration):
        n = len(filtration.simplices)
        B = [set() for _ in range(n)] 

        simplex_map = {s.verts: i for i, s in enumerate(filtration.simplices)}
        
        for j, simplex in enumerate(filtration.simplices):
            if simplex.dim > 0:
                boundary_faces = simplex.boundary()
                for face in boundary_faces:
                    if face.verts in simplex_map:
                        i = simplex_map[face.verts]
                        B[j].add(i) 
        
        return BoundaryMatrix(B)
    
    def write_sparse_boundary_matrix_to_file(self, output_filename):
        with open(output_filename, 'w') as file:
            for j, col in enumerate(self.B):
                boundaries = sorted(list(col)) 
                line = f"Column {j}: " + " ".join(map(str, boundaries)) + "\n"
                file.write(line)