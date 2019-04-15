from collections import defaultdict

def findOrder(numCourses, prerequisites):
    in_deg = [0] * numCourses
    edges = defaultdict(list)
    queue = []
    for edge in prerequisites:
        in_deg[edge[0]] += 1
        edges[edge[1]].append(edge[0])
    queue = [i for i in range(numCourses) if in_deg[i] == 0]

    num = 0
    top = []
    while queue:
        node = queue.pop(0)
        # top[node] = num
        top.append(node)
        # num += 1
        for neighbor in edges[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)

    if len(top) != numCourses:
        return []
    return top
    

if __name__ == "__main__":
    print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
