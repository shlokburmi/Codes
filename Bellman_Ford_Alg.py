def bellmanford(vertices, edges, source):
     dist=[float('inf')]*vertices
     dist[source]=0
     
     for i in range(vertices-1):
          for u,v,w in edges:
               if(dist[u-1] != float('inf') and dist[u-1]+w<dist[v-1]):
                    dist[v-1]=dist[u-1]+w
     for i in range(vertices):
          print("vertex",i,"Distance from source:",dist[i])
vertices=7
edges=[
     (1,2,6),
     (1,3,5),
     (1,4,5),
     (2,5,-1),
     (3,2,-2),
     (4,3,-2),
     (3,5,1),
     (4,6,-1),
     (5,7,3), 
     (6,7,3)
]
source=0
bellmanford(vertices,edges,source)
