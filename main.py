from data_classes.boundary_matrix import BoundaryMatrix
from data_classes.filtration import Filtration

def build_boundary_matrix(filename):
    filtration = Filtration.read_filtration(filename)
    return BoundaryMatrix.build_sparse_boundary_matrix(filtration)

def Q1():
    filename = "filtrations_data/filtration_A.txt"
    output_filename = "output_data/boundary_matrix_A.txt"
    B = build_boundary_matrix(filename)
    BoundaryMatrix.write_sparse_boundary_matrix_to_file(B, output_filename)

if __name__ == '__main__':
    Q1()