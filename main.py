from data_classes.boundary_matrix import BoundaryMatrix
from data_classes.filtration import Filtration
from data_classes.barcode import Barcode

def Q1():
    filename = "filtrations_data/filtration_A.txt"
    output_filename = "output_data/boundary_matrix_A.txt"
    filtration = Filtration.read_filtration(filename)
    B = BoundaryMatrix.build_sparse_boundary_matrix(filtration)
    BoundaryMatrix.write_sparse_boundary_matrix_to_file(B, output_filename)

def Q2():
    filename = "filtrations_data/test.txt"
    output_filename = "output_data/test.txt"
    method = 'optimal'
    filtration = Filtration.read_filtration(filename)
    B = BoundaryMatrix.build_sparse_boundary_matrix(filtration)
    barcode = Barcode.generate_barcode(filtration.simplices, B, method)
    barcode.write_barcode_to_file(output_filename)

if __name__ == '__main__':
    #Q1()
    Q2()