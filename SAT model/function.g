
RemoveIsoImages := function(GraphList, GraphImage)
local len, i, element;
i := 0;
len := Length(GraphList);
for element in GraphList do
i := i + 1;
if IsIsomorphicDigraph(element, GraphImage) then
Remove(GraphList, i);
fi;
od;
return GraphList;
end;

IsoFreeGraphs := [Graphs[1]];

for element in Graphs do
Graphs := RemoveIsoImages(Graphs, element);
Add(IsoFreeGraphs, Graphs[1]);
od;

SaveWorkspace("workspace.g");
PrintTo("result.g", Length(IsoFreeGraphs));
quit;
