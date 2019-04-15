from collections import defaultdict
def canFinish(numCourses, prerequisites):
    in_deg = [0] * numCourses
    edges = defaultdict(list)
    queue = []
    for edge in prerequisites:
        in_deg[edge[1]] += 1
        edges[edge[0]].append(edge[1])
    queue = [i for i in range(numCourses) if in_deg[i] == 0]
    
    num = 0 
    top = {}
    while queue:
        node = queue.pop(0)
        top[node] = num
        num += 1
        for neighbor in edges[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0: queue.append(neighbor)

    if len(top) == numCourses: return True
    
    return False


def canFinish2(numCourses, prerequisites):
    
    def dfs(i, visited, edges):
            # print(f'dfs {i}')
            visited[i] = -1
            for neighbor in edges[i]:
                if visited[neighbor] == -1:
                    return False
                elif visited[neighbor] == 0:
                    if not dfs(neighbor, visited, edges):
                        return False
            visited[i] = 1
            return True

    visited = [0] * numCourses
    edges = defaultdict(list)
    for edge in prerequisites:
        edges[edge[0]].append(edge[1])

    for i in range(numCourses):
        if not dfs(i, visited, edges):
            return False
    return True

if __name__ == "__main__":
    # print(canFinish2(2, [[1, 0]]))
    # print(canFinish2(2, [[1, 0], [0, 1]]))
    print(canFinish2(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
