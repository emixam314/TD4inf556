import time
from data_classes.boundary_matrix import BoundaryMatrix
from data_classes.filtration import Filtration
from data_classes.barcode import BarcodeGenerator

def Q1():
    filename = "filtrations_data/test.txt"
    output_filename = "output_data/boundary_matrix_test.txt"
    filtration = Filtration.read_filtration(filename)
    B = BoundaryMatrix.build_sparse_boundary_matrix(filtration)
    BoundaryMatrix.write_sparse_boundary_matrix_to_file(B, output_filename)

def Q4():
    """Generates the barcode for the given filtration and writes it to a file."""

    filename = "filtrations_data/test.txt"
    output_filename = "output_data/test.txt"
    method = 'naive'
    filtration = Filtration.read_filtration(filename)
    B = BoundaryMatrix.build_sparse_boundary_matrix(filtration)
    barcode_generator = BarcodeGenerator(B, filtration, method)
    barcode_generator.generate_barcode()
    barcode_generator.write_barcode_to_file(output_filename)

def Q7():
    
    for letter in ['A','B','C','D']:
        filename = f"filtrations_data/filtration_{letter}.txt"
        output_filename = f"output_data/filtration_{letter}.txt"
        method = 'optimal'
        filtration = Filtration.read_filtration(filename)
        B = BoundaryMatrix.build_sparse_boundary_matrix(filtration)
        start = time.time()
        barcode_generator = BarcodeGenerator(B, filtration, method)
        barcode_generator.generate_barcode()
        end = time.time()
        print(f"Barcode generation for filtration {letter} took {end-start} seconds.")
        barcode_generator.write_barcode_to_file(output_filename)





if __name__ == '__main__':
    #Q1()
    Q4()
    #Q7()