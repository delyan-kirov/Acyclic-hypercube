LoadPackage("Digraph"); 
G6 := DigraphByAdjacencyMatrix([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]);
G15 := DigraphByAdjacencyMatrix([[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]);
G17 := DigraphByAdjacencyMatrix([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]);

PrintTo("output.g", IsIsomorphicDigraph(G6, G15));
