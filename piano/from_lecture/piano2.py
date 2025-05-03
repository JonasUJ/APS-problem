
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

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

def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity # set to 0 to disable capacity scaling
    while True:
        #ispath, p_or_seen = bfs(graph,src,dest,mincap)
        ispath, p_or_seen = dfs(graph,src,dest,mincap, set())
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


testcases = int(input())
start = 0
sink = 3000

for _ in range(testcases):
    graph = defaultdict(lambda: defaultdict(int))
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
        graph[start][day]=workforce
        
        for piano in days_to_piano_weekdays[day]:
            graph[day][piano]=1
            graph[piano][sink]=1

    for day in days_to_piano_weekend:
        graph[start][day]=workforce
        
        for piano in days_to_piano_weekend[day]:
            graph[day][piano]=1
            graph[piano][sink]=1
    
    flow_value, residual_graph, x = flow(graph, start, sink)
    
    if flow_value < pianos:
        print("serious trouble")
        break

    weekend_work = False
    filter_days = {k: v for k, v in residual_graph.items() if 1 <= k <= 100}
    for day in filter_days:
        #print(day)
        if day % 7 == 0 or day % 7 == 6:
            if filter_days[day]:
                weekend_work = True
                break
    
    if weekend_work: 
        print("weekend work")
    else:
        print("fine")
 

