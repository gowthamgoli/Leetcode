from collections import defaultdict

def findRedundantConnection(edges):

    def dfs(num, edge_list, visited, parent, dfn, dfn_num, redundant):
        # print(f'dfs {num}')
        visited[num] = True
        dfn[num] = dfn_num
        dfn_num += 1
        for neighbor in edge_list[num]:
            if not visited[neighbor]:
                parent[neighbor] = num
                dfs(neighbor, edge_list, visited, parent, dfn, dfn_num, redundant)
            elif parent[num] != neighbor and dfn[num] < dfn[neighbor]: 
                redundant.append([min(num, neighbor), max(num, neighbor)])
    edge_list = defaultdict(list)
    n = 0
    for edge in edges: 
        n = max(n, max(edge))
        edge_list[edge[0]].append(edge[1])
        edge_list[edge[1]].append(edge[0])
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    dfn = [0] * (n + 1)
    redundant = []
    dfs(1, edge_list, visited, parent, dfn, 1, redundant)
    return redundant[-1]

def findRedundantConnection2(edges):
    parent = [0] * (len(edges) + 1)

    def find_root(x):
        if parent[x] == 0:
            return x
        return find_root(parent[x])

    def union(x, y):
        root_x = find_root(x)
        root_y = find_root(y)
        if root_x == root_y:
            return False
        parent[root_x] = root_y
        return True
    for (x, y) in edges:
        if not union(x, y):
            return [x, y]

if __name__ == "__main__":
    # edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [5, 6], [5, 7], [1, 7], [6, 7]]
    # print(findRedundantConnection2(edges))
    edges = [[1, 2], [1, 3], [2,3]]
    print(findRedundantConnection2(edges))

