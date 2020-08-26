class deBruijnGraph(object):
    def __init__(self, reads):
        self.nodes={}
        for read in reads:
            left=read[:-1]
            right=read[1:]
            if left not in self.nodes:              
                self.nodes[left]=[]
            if right not in self.nodes:              
                self.nodes[right]=[]
            self.nodes[left].append(right)
            
    def getSuperstring(self):
        counter=0
        visited=[]
        start_node=next(iter(self.nodes)) 
        node=start_node
        superstring=""
        while node not in visited:
            if node not in self.nodes: return None
            if len(self.nodes[node])!=1: return None
            superstring+=node[-1]
            visited.append(node)
            node=self.nodes[node][0]  
        return superstring if node==start_node else None

reads=['ATTAC', 'TACAG', 'GATTA', 'ACAGA', 'CAGAT', 'TTACA', 'AGATT']
print("reads:", reads)
gr=deBruijnGraph(reads)
print("superstring:", gr.getSuperstring())