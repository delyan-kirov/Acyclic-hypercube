from itertools import product

# specify the number of vertices
n = 7

vertices = [f'a{i + 1}' for i in range(n)]
edges = [(vertices[i], vertices[(i + 1) % n]) for i in range(n)]

def generate_possibilities(vertices, edges):
    directions = list(product([True, False], repeat=len(edges)))
    possibilities = []
    for direction in directions:
        possibility = []
        for i in range(len(edges)):
            if direction[i]:
                possibility.append(f'(C(({edges[i][0]},{edges[i][1]})) = 1)')
            else:
                possibility.append(f'(C(({edges[i][1]},{edges[i][0]})) = 1)')
        possibilities.append(' /\ '.join(possibility))
    return possibilities

possibilities = generate_possibilities(vertices, edges)

with open('nGon.txt', 'w') as f:
    for possibility in possibilities:
        f.write("(" + possibility + ') \/ \n')