from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

# all graphs are (default) dictionaries
# vertex -> (vertex -> capacity), by default capacity is 0


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


if __name__ == "__main__":
    testcases = int(input())
    start = 0
    sink = 2000

    for _ in range(testcases):
        graph = defaultdict(lambda: defaultdict(int))
        pianos, movers = map(int, input().split())
        days = set() #set of days for moving
        
    
        for i in range(pianos):
            piano_id = 1000+i 
            graph[start][piano_id] = 1 #edge from start to piano

            start_date, end_date = map(int, input().split())
            """
            
            temp = []
            for day in range(start_date, end_date+1):
                if day % 7 == 0 or day % 7 == 6:
                    temp.append(day)

                else:
                    days.add(day)
                    graph[piano_id][day] = 1

            for day in temp:
                    days.add(day)
                    graph[piano_id][day] = 1
            
        for day in days: 
            graph[day][sink] = movers//2 #capacity for each day
            """

            weekday_days = []
            weekend_days = []
            for day in range(start_date, end_date+1):
                if day % 7 == 0 or day % 7 == 6:  # Weekend (Sunday=0, Saturday=6)
                    weekend_days.append(day)
                else:
                    weekday_days.append(day)

            # Add weekday edges first
            for day in weekday_days:
                days.add(day)
                graph[piano_id][day] = 1

            # Add weekend edges after
            for day in weekend_days:
                days.add(day)
                graph[piano_id][day] = 1
        
        for day in days: 
            graph[day][sink] = movers//2 #capacity for each day


        flow_value, residual_graph, x = flow(graph, start, sink) 
        #print(flow_value)
        
        if(pianos>flow_value):
           # print(residual_graph)
            print("serious trouble")
        else:
            weekendwork = False
            #print(residual_graph)
            for node in residual_graph:
                if 0 < node < 101: #get the days nodes
                    if node % 7 == 6 or node % 7 == 0: #get the weekdays
                        if residual_graph[node]: #check if the weekendday is used
                            weekendwork = True
            if (weekendwork):
                print("weekend work")    
            else:
                print("fine")         
            #i need to figure out if weekend has been used

    
    """
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    graph = defaultdict(lambda: defaultdict(int))
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u][v] = c

    flow_value, residual_graph, _ = flow(graph, s, t)
    print(flow_value)
    """