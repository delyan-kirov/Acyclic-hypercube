# %%
import math
import os
import re

# %%
#Creates the adj matrix arrays for the graphs
def make_data(files):
    with open(files, "r") as file:
        cover = file.read()
        graph_data = ""
        # finding pattern
        pattern = re.compile(r"--> (\d+)")
        for match in pattern.finditer(cover):
            number = match.group(1)
            graph_data = "".join((graph_data, number))
    pass
    return list(graph_data)

# %%
#Creates the data for gap to read and do computations.
def gap_input(data:list, count:int):
     dimension = int(math.sqrt(len(data)))
     vectors = [data[i:i+dimension] for i in range(0, len(data), dimension)]
     matrix = []
     for vec in vectors:
          matrix.append(list(map(int, vec)))

     gap_data = "G" + str(count) + " := " + "DigraphByAdjacencyMatrix(" + str(matrix) + ");" + "\n"
     return gap_data

# %%
# Adds the graphs to an array in gap
def init_graphs_array(filename:str):
    with open(filename, 'r') as f:
        data = f.read()
        f.close

    graphs = []
    #Annoying pattern matching to find the graphs and store them in an array for gap. 
    while data != "":
        start = '; \n'
        end = ' := '
        if re.search('%s(.*)%s' % (start, end), data) is None: break
        result = re.search('%s(.*)%s' % (start, end), data).group(1)
        data = data.split(result, 1)[1]
        data = data.split(";", 1)[1]
        graphs.append(result)
        data = "garbage; " + data
    output = "\n Graphs := " + str(graphs).replace("'", "") + "; \n"
    return output


# %%
# main
count = 0
funct = ""

with open("function.g", 'r') as f:
        funct = f.read()
        f.close

gap = "LoadPackage(\"Digraph\"); \n"
for files in os.listdir("."):
        count = count + 1
        if files.endswith(".solution"):
             gap = gap + gap_input(make_data(files), count)

with open('data.g', 'w') as f:
    f.write(gap)

init_graphs_array("data.g")
with open("data.g", 'a') as f:
        f.write(init_graphs_array("data.g"))
        f.write(funct)
        f.close
