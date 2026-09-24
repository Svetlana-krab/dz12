#Double-Degree Array
def neighbor_degree_sum(n,edges):
    adj=[[]for l in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    degree = [len(adj[i]) for i in range(n+1)]
    return [sum(degree[j] for j in adj[i]) for i in range(1,n+1)]
n,m = map(int,input().split())
edges = [tuple(map(int, input().split())) for l in range(m)]
result= neighbor_degree_sum(n, edges)
print(*result)