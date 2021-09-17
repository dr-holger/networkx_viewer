import networkx as nx
from networkx_viewer import Viewer

### Example 3 ###
G = nx.MultiDiGraph()
G = nx.read_graphml("test.graphml")
app = Viewer(G)
app.mainloop()