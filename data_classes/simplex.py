class Simplex:

    def __init__(self, val, dim, verts):
        self.val = val   
        self.dim = dim   
        self.verts = tuple(sorted(verts)) 

    def boundary(self):
        if self.dim == 0:
            return [] 
        boundaries = []
        for i in range(len(self.verts)):
            face = self.verts[:i] + self.verts[i+1:]
            boundaries.append(Simplex(self.val, self.dim - 1, face))
        return boundaries

    def read_filtration(filename):
        simplices = []
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                val = float(parts[0])
                dim = int(parts[1])
                verts = list(map(int, parts[2:]))
                simplices.append(Simplex(val, dim, verts))
        return simplices
