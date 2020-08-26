class WeightedGraph(object):
    def __init__(self, edges):
        self.edges=edges
        self.nodes=set()
        for edge in edges:
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
            
    def getShortestPathArray(self):
        dist={}
        for u in self.nodes:
            dist[u]='x'
            
        dist[1]=0
        nodes_count=len(self.nodes)
        for i in range(nodes_count):
            for edge in self.edges:
                u=edge[0]
                v=edge[1]
                weight=edge[2]
                if dist[u]!='x' and (dist[v]=='x' or dist[v]>dist[u]+weight):
                    if i==nodes_count-1:
                        print('Negative cycle present!')
                        return []
                    
                    dist[v]=dist[u]+weight
        return dist

ex1_edges=[(1,2,4),(1,3,3),(2,4,4),(4,5,2),(3,5,1),(2,3,-2),(3,4,-3),(6,6,5)]
ex1=WeightedGraph(ex1_edges)
print(ex1_edges)
print("Shortest path array:", ex1.getShortestPathArray())

ex2_edges=[(1,2,4),(1,3,3),(2,4,4),(4,5,2),(3,5,1),(2,3,-2),(3,4,-3),(4,2,-5)]
ex2=WeightedGraph(ex2_edges)
print(ex2_edges)
print("Shortest path array:", ex2.getShortestPathArray())