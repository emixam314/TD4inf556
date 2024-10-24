from data_classes.simplex import Simplex

class Filtration:

    def __init__(self, simplices:list[Simplex]):
        self.simplices = simplices

    def sort_simplices(self):
        return sorted(self.simplices, key=lambda s: (s.val, s.dim))
    
    @staticmethod
    def read_filtration(filename):
        simplices = []
        print(filename)
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                val = float(parts[0])
                dim = int(parts[1])
                verts = list(map(int, parts[2:]))
                simplices.append(Simplex(val, dim, verts))
        return Filtration(simplices)