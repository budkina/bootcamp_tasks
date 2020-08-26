class SimpleGraph(object):
    def __init__(self, edges):
        self.nodes={}
        for edge in edges:
            v1=edge[0]
            v2=edge[1]
            if v1 not in self.nodes:              
                self.nodes[v1]=[]
            if v2 not in self.nodes:              
                self.nodes[v2]=[]
                
            self.nodes[v1].append(v2)
            self.nodes[v2].append(v1)
            
    def visit(self,root_node):
        self.visited.add(root_node)
        v_adj=self.nodes[root_node]
        for v in v_adj:
            if v not in self.visited:
                self.visit(v)

    def getComponentsNum(self):
        self.visited=set()
        components_num=0
        for node in self.nodes:
            if node not in self.visited:
                components_num+=1
                self.visit(node)
        return components_num
        
ex1_edges=[(1,2),(1,3),(4,5),(5,6),(7,7)]
ex1=SimpleGraph(ex1_edges)
components_num=ex1.getComponentsNum()
print(ex1_edges)
print("Connected components:", components_num)

ex2_edges=[(1,1),(1,1),(2,2),(2,2),(2,2)]
ex2=SimpleGraph(ex2_edges)
components_num=ex2.getComponentsNum()
print(ex2_edges)
print("Connected components:", components_num)