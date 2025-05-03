from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
def bfs(graph,src,dest,mincap=0): # returns path to dest or reachable set
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > mincap and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))

def flow(orggraph, src,dest, pianos):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity # set to 0 to disable capacity scaling
    while True:

        ispath, p_or_seen = bfs(graph,src,dest,mincap)
        #ispath, p_or_seen = dfs(graph,src,dest,mincap, set())
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
      
        p = p_or_seen
       #print("path:", *reversed(p))
        saturation = min( graph[u][v] for u,v in p )
        #print(current_flow,saturation)#,[f"{u[0]}-{u[1]}:{orggraph[u[0]][u[1]]}:{graph[u][v]}" for u,v in p if u[2]==0])
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation
        
        #print(current_flow)
    
        if (current_flow == pianos):
            #print("sup")
            return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
        
# 2 graph solution
testcases = int(input())
for _ in range(testcases):
    graph_weekdays = defaultdict(lambda: defaultdict(int))
    graph_alldays = defaultdict(lambda: defaultdict(int))
    pianos, movers = map(int, input().split())
    
    days_to_piano_weekdays = defaultdict(set)
    days_to_piano_weekend = defaultdict(set)

    for i in range(pianos):
        piano_id = 1000+i 
        #graph[start][piano_id] = 1 #edge from start to piano
        
        start_date, end_date = map(int, input().split())

        for day in range(start_date, end_date + 1):
            if day % 7 == 0 or day % 7 == 6:
                days_to_piano_weekend[day].add(piano_id)
            else:
                days_to_piano_weekdays[day].add(piano_id)   
    
    start = 0
    sink = 3000
    workforce = movers//2

    for day in days_to_piano_weekdays:
        graph_weekdays[start][day]=workforce
        graph_alldays[start][day]=workforce
        
        for piano in days_to_piano_weekdays[day]:
            graph_weekdays[day][piano]=1
            graph_weekdays[piano][sink]=1

            graph_alldays[day][piano]=1
            graph_alldays[piano][sink]=1

    for day in days_to_piano_weekend:
        graph_alldays[start][day]=workforce
        
        for piano in days_to_piano_weekend[day]:
            graph_alldays[day][piano]=1
            graph_alldays[piano][sink]=1
    
    
    flow_value, residual_graph, x = flow(graph_weekdays, start, sink)
    if flow_value < pianos:
        flow_value, residual_graph, x = flow(graph_alldays, start, sink)
        
        if flow_value < pianos:
            print("serious trouble")
        else:
            print("weekend work")
    else:
        print("fine")