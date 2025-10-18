def connectedComponents(n, edges):
    mat = [[] for _ in range(n)]
    for i , j in edges:
        mat[i].append(j)
        mat[j].append(i)
        def dfs(node):
            visited[node] = True
            for val in mat[node]:
                if not visited[val]:
                    visited[val] = True
                    dfs(val)
        ans = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans+=1
    return ans
