# [Urban Company](http://www.urbancompany.com/)

## Details

### Job status

Full Time( Employment + Internship Mandatory)

31/07/23

### Criteria

|Study|Cutoff|
|-----|------|
|UG|8GPA|

### Compensation

||FTE|Internship|
|--|-----|------|
|Base|16,00,000|50000|
|ESOP vested across 4 years|8,00,000|--|
|Joining Bonus|3,00,000|--|
|Retention Bonus|3,00,000|--|

## OA

### Questions

1. **Black and White tree**: Given a tree with N vertices labeled 1-N rooted at 1. The tree is an undirected graph with N-1 edges. Each edge i connects two vertices ai and bi. Each vertex i is colored either white (0) or black (1).

    The beauty of a vertex i is the number of paths in its subtree that have end vertices of the opposite color.

    Find the beauty of all N vertices.

    - *Note*: A subtree of a vertex i is a connected sub-graph consisting of all the descendants of i including i.

> Perform dfs and get number of blacks and whites at each vertex and multiply them and store in dp.

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> dfs(int i, vector<vector<int>>& graph, unordered_set<int>& visited, vector<int>& result) {
    if (visited.find(i) != visited.end()) {
        return {0, 0};
    }
    visited.insert(i);
    int black = 0, white = 0;
    vector<int> numC;
    for (auto j: graph[i]) {
        numC = dfs(j, graph, visited, result);
        black += numC[0];
        white += numC[1];
    }
    string[i - 1] == '1' ? ++black : ++white;
    result[i - 1] = black * white;
    return {black, white};
}

vector<int> solve(int N, string Color, vector<vector<int>> Edges) {
    vector<vector<int>> graph(N + 1);
    unordered_set<int> visited;
    vector<int> result(N);
    
    for (auto edge: Edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }
    
    dfs(1, graph, visited, result);
    return result;
}
```

> This TLE'd by 0.005s for 3 cases while the other 7 passed.

2. [Minimum Value](https://codeforces.com/problemset/problem/360/B)

3. [Falling Apples](https://www.thejoboverflow.com/problem/147/)

---
