# %%
import math
import os
import re

# %%
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
def gap_input(data:list, count:int):
     dimension = int(math.sqrt(len(data)))
     vectors = [data[i:i+dimension] for i in range(0, len(data), dimension)]
     matrix = []
     for vec in vectors:
          matrix.append(list(map(int, vec)))

     gap_data = "G" + str(count) + " := " + "Digraph(" + str(matrix) + ");" + "\n"
     return gap_data


# %%
# main
count = 0
gap = "LoadPackage(\"Digraph\"); \n"
for files in os.listdir("."):
        count = count + 1
        if files.endswith(".solution"):
             gap = gap + gap_input(make_data(files), count)

with open('data.g', 'w') as f:
    f.write(gap)
