from itertools import product

vertices = ['i', 'j', 'k', 'l', 'm']
edges = [('i', 'j'), ('j', 'k'), ('k', 'l'), ('l', 'm'), ('m', 'i')]

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

with open('pentagon.txt', 'w') as f:
    for possibility in possibilities:
        f.write("(" + possibility + ') \/ \n')