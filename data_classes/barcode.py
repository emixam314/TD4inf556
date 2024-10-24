from methods.reductions import Reduction, Optimal_reduction, Naive_reduction

class Barcode:

    def __init__(self, barcode):
        self.barcode = barcode

    @staticmethod
    def generate_barcode(simplices, B, method='optimal'):
        barcode = []
        
        B = Optimal_reduction(B).reduce_boundary_matrix() if method == 'optimal' else Naive_reduction(B).reduce_boundary_matrix()

        for j, simplex in enumerate(simplices):
            pivot = Reduction(B).low_pivot(j)
            if pivot is None:
                barcode.append((simplex.dim, simplex.val, float('inf'))) 
            else:
                death_time = simplices[pivot].val
                barcode.append((simplex.dim, simplex.val, death_time))

        return Barcode(barcode)


    def write_barcode_to_file(self, output_filename):
        with open(output_filename, 'w') as file:
            for dim, birth, death in self.barcode:
                file.write(f"{dim} {birth} {death}\n")