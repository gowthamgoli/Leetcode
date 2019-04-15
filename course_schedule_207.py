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

if __name__ == "__main__":
    canFinish(2, [[1, 0]])
    canFinish(2, [[1, 0], [0, 1]])
