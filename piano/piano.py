from collections import defaultdict
import sys
import time

sys.setrecursionlimit(10**6)
def dfs(graph,u,dest,seen): # returns path to dest
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > 0: # only consider edges with capacity > mincap
            if v == dest:
                return (True,[(u,v)])
    
            suc, p = dfs(graph,v,dest,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)

def flow(orggraph, src,dest, pianos):
    graph = defaultdict(lambda: defaultdict(int))
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c

    current_flow = 0
    
    while True:
        ispath, p_or_seen = dfs(graph,src,dest, set())
        #ispath, p_or_seen = bfs(graph,src,dest)
        if not ispath:
            return current_flow
      
        p = p_or_seen
        saturation = 1
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation
    
        if (current_flow == pianos):
            return current_flow
        
# 2 graph solution
testcases = int(input())
for _ in range(testcases):
    graph_weekdays = defaultdict(lambda: defaultdict(int))
    graph_weekends = defaultdict(lambda: defaultdict(int))
    pianos, movers = map(int, input().split())
    
    days_to_piano_weekdays = defaultdict(set)
    days_to_piano_weekend = defaultdict(set)

    for i in range(pianos):
        piano_id = 1000+i         
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
        
        for piano in days_to_piano_weekdays[day]:
            graph_weekdays[day][piano]=1
            graph_weekdays[piano][sink]=1

    for day in days_to_piano_weekend:
        graph_weekends[start][day]=workforce
        
        for piano in days_to_piano_weekend[day]:
            graph_weekends[day][piano]=1
            graph_weekends[piano][sink]=1
    
    
    flow_value_weekdays = flow(graph_weekdays, start, sink, pianos) 
    if flow_value_weekdays < pianos:
        flow_value_weekend = flow(graph_weekends, start, sink, pianos-flow_value_weekdays)

        if flow_value_weekdays+flow_value_weekend < pianos:
            print("serious trouble")
            continue
        else:
            print("weekend work")
            continue
    else:
        print("fine")
        continue

