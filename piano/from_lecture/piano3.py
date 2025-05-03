
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

def dfs(graph,u,dest,mincap,seen): # returns path to dest
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > mincap: # only consider edges with capacity > mincap
            if v == dest:
                return (True,[(u,v)])
            #print(f'explore {u} {v}, {cap}')
            suc, p = dfs(graph,v,dest,mincap,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)

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


"""

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

"""
"""
# scale up weekends 
testcases = int(input())
for _ in range(testcases):
    graph = defaultdict(lambda: defaultdict(int))
    pianos, movers = map(int, input().split())
    days = set()
    sink = 3000
    start = 0
    scale = 1000

    for i in range(pianos):
        piano_id = 1000+i 
        graph[start][piano_id] = 1 * scale
        
        start_date, end_date = map(int, input().split())
        for day in range(start_date, end_date + 1):
            days.add(day)
            if day % 7 == 0 or day % 7 == 6:
                graph[piano_id][day] = 1 * scale +1
            else:
                graph[piano_id][day] = 1 * scale
        
    for day in days: 
        graph[day][sink] = ((movers//2) * scale)
    
    
    flow_value, residual_graph, x = flow(graph, start, sink, pianos)

    print(residual_graph)
"""


 # adding extra nodes for weekends (does not work)
testcases = int(input())
for _ in range(testcases):
    graph = defaultdict(lambda: defaultdict(int))
    pianos, movers = map(int, input().split())
    days = set()
    sink = 4000
    start = 0

    for i in range(pianos):
        piano_id = 1000+i 
        piano_id2 = piano_id+1000
        graph[start][piano_id] = 1
        
        start_date, end_date = map(int, input().split())
        for day in range(start_date, end_date + 1):
            days.add(day)
            if day % 7 == 0 or day % 7 == 6:
                graph[piano_id][piano_id2] = 1
                graph[piano_id2][day] = 1

            else:
                graph[piano_id][day] = 1
            
    for day in days: 
        graph[day][sink] = movers//2 #capacity for each day
    
    
    flow_value, residual_graph, x = flow(graph, start, sink, pianos)
    if(pianos>flow_value):
        # print(residual_graph)
        print("serious trouble")
    else:
        weekendwork = False
        #print(residual_graph)
        for node in residual_graph:
            if 0 < node < 101 and node % 7 in {0, 6}:
                if residual_graph[node]: #check if the weekendday is used
                    weekendwork = True
        if (weekendwork):
            print("weekend work")    
        else:
            print("fine")   
