from methods.reductions import Reduction, Optimal_reduction, Naive_reduction
from data_classes.boundary_matrix import BoundaryMatrix
from data_classes.filtration import Filtration

# class Barcode:

#     def __init__(self, barcode):
#         self.barcode = barcode

#     @staticmethod
#     def generate_barcode(simplices, B, method='optimal'):
#         barcode = []
        
#         reduced_matrix = Optimal_reduction(B).reduce_boundary_matrix() if method == 'optimal' else Naive_reduction(B).reduce_boundary_matrix()

#         barcode = []  # To hold the barcode intervals
#         birth_dict = {}  # To track birth times of features

#         # Process the reduced boundary matrix
#         for k in range(len(reduced_matrix.B)):
#             for row in reduced_matrix.B[k]:
#                 if len(row) == 0:  # No features in this dimension
#                     continue
                
#                 # Assuming the first non-empty entry corresponds to a generator (birth)
#                 birth_time = simplices[k]
#                 birth_dict[k] = birth_time

#                 # Iterate through the row to find death times
#                 for death_row in row:
#                     if death_row in birth_dict:  # Feature killed
#                         death_time = simplices[death_row]
#                         birth = birth_dict[dim]  # Get birth from dictionary
#                         barcode.append((dim, birth, death_time))

#         return barcode

class BarcodeGenerator:
    def __init__(self, boundary_matrix: BoundaryMatrix, filtration: Filtration, method='optimal'):
        if method == 'optimal':
            self.boundary_matrix =  Optimal_reduction(boundary_matrix).reduce_boundary_matrix()  
        elif method=='naive':
            self.boundary_matrix = Naive_reduction(boundary_matrix).reduce_boundary_matrix() 
        self.filtration = filtration
        self.barcode = []

    def generate_barcode(self):
        """Generates the barcode from the reduced boundary matrix."""
        birth_times = {}
        active_features = {}
        for j in range(len(self.boundary_matrix.B)):
            pivot = self.boundary_matrix.low_pivot(j)

            if pivot is None:
                birth_time = self.filtration.simplices[j].val
                dim = self.filtration.simplices[j].dim
                active_features[j] = (birth_time, dim)
            else:
                if pivot in active_features:
                    death_time = self.filtration.simplices[j].val

                    self.barcode.append(
                        (active_features[pivot][1], active_features[pivot][0], death_time)
                    )

                    del active_features[pivot]

        for j, (birth_time, dim) in active_features.items():
            if j in active_features:
                self.barcode.append((dim, birth_time, float('inf')))


    def write_barcode_to_file(self, output_filename):
        with open(output_filename, 'w') as file:
            for dim, birth, death in self.barcode:
                file.write(f"{dim} {birth} {death}\n")