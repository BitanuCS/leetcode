
def creategraph(v, edges):
    adj = [[] for _ in range(v + 1)]

    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        adj[v].append(u)

    return adj


def print_graph(adj):
    print("Adjacency List Representation:")
    for i in range(1, len(adj)):
        print(f"{i}:", *adj[i])
