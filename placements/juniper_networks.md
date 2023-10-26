# [Juniper Networks](https://www.juniper.net)

## Details

### Job Status

Internship + PPO

### Criteria

| Study | Cutoff  |
|-------|---------|
| X     | %       |
| XII   | %       |
| UG    | 7.5 GPA |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE   | Internship |
|--------|-------|------------|
| Base   | 14.5L | 40000      |
| Stocks | --    | --         |
| Bonus  | 2L    | --         |
| CTC    | 16.5L | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 26/10/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 14 questions in total to be solved in 110 min.

1. MCQ (11) - Comprehension, Aptitude, Technical
2. Coding (3)

### Coding Questions

1. **Decorate Function**: Write a single decorator for 3 functions, which have variable arguements and one key value arguement `delay`.

    There exists a global list `execution_time` which should include a number close to the delay_time for each query.
    
    The function being decorated should return its respective value.

    Example:
    ```
    3 --> Number of queries
    delay_max 1 2 3 100
    delay_min 3 4 1 7 200
    delay_sum 2 2 300

    Output
    3
    1
    4
    [100,200,300]
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
# Pre-defined functions
def delay_max(*args, **kwargs):
    time.sleep(kwargs["delay"] / 1000)
    return max(args)


def delay_min(*args, **kwargs):
    time.sleep(kwargs["delay"] / 1000)
    return min(args)


def delay_sum(*args, **kwargs):
    time.sleep(kwargs["delay"] / 1000)
    return sum(args)


execution_time = []
#
# Complete the 'timeit' function below.
#
# The function is expected to return a function.
# The function accepts following parameter:
#  1. FUNCTION func
#

def timeit(func: Callable) -> Callable:
    # Write your code here
    def wrapper(*args, **kwargs):
        execution_time.append(kwargs["delay"])
        return func(*args, **kwargs)
    return wrapper
```

---

2. **CPP Constructor**: Given an empty class, this class will be called with the `()` operator, limit the number of times this operator is called.

    If the number of calls exceeds this limit, throw -1 as the error.

    The class also has a public method `get_sum()` which should return the total sum of all the arguements passed during the multiple `()` operator call.

    Example:
    ```cpp
    xcallable obj_1(3);
    obj_1(3)(4)(5); // Output 12

    xcallable obj_2(3);
    try {
        obj_2(3)(4)(5)(6);
    }
    catch (int x) {
        std::cout << "Exception called" << std::endl;
    }
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
class xcallable{
private:
    int called = 0;
    int limit;
    int argsum = 0;
public:
    xcallable(int limit) {
        this->limit = limit;
    }
    
    xcallable& operator ()(int arg) {
        ++called;
        if (called > limit) {
            throw -1;
        }
        argsum += arg;
        return *this;
    }
    int get_sum() {
        return argsum;
    }
};
```
---

3. **Recover Dead Pods**: There are n nodes from 1-n. Some of these nodes are connected to each other. This is represented with a list of undirected edges between two nodes. Nodes that are directly or indirectly connected to each other are part of the same region.

    Each node has their respective database connection, such that whenever a query is called, it will record it in their respective database.

    There are q queries, each query of the following type:

    1. "1 pod_id": Represents a normal query to the node pod_id.
    2. "2 pod_id": Represents a disconnect to the database for the mentioned pod_id. (This disconnect is irreversible, once disconnected, cannot be reconnected)

    If a query is for a node whose database connection is down (due to a prior database disconnect query), this query is forwarded to the smallest valued node in the region the initial requested node belongs to and is written to that node's database. Return the node which makes the database call. (Smallest if requested is down, else the requested node).

    If the query is for a node whose database connection is down, and every other node in its region is also down, then the query is not written and is lost. In this case, return -1.

    Example:
    ```
    5 --> Nodes
    3 --> Connections
    1 2
    2 3
    4 5

    6 --> Queries
    1 4
    2 2
    1 2
    2 3
    2 1
    1 1

    Output:
    [4,1,-1]

    Explanation:
    1 4 --> The requested node is alive, hence written to that database.
    2 2 --> Node 2 lost its database connection.
    1 2 --> Node 2 doesn't have an active database connection, it belongs to the region whose smallest valued node is 1, hence written to 1.
    2 3 --> Node 3 lost its database connection.
    2 1 --> Node 1 lost its database connection.
    1 1 --> Node 1 doesn't have an active database connection and other nodes in its region are down, hence -1.
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
class DSU {
private:
    vector<int> parents, rank;
    int n;
public:
    DSU(int n) {
        this->n = n;
        parents = vector<int>(n + 1);
        rank = vector<int>(n + 1, 1);
        iota(parents.begin(), parents.end(), 0);
    }
    
    int find(int u) {
        if (parents[u] == u) {
            return u;
        }
        return parents[u] = find(parents[u]);
    }
    
    void join(int u, int v) {
        int up = find(u);
        int vp = find(v);
        
        if (up == vp) {
            return;
        }
        
        if (rank[up] > rank[vp]) {
            parents[vp] = up;
        }
        else {
            parents[up] = vp;
            ++rank[vp];
        }
    }
};

vector<int> recoverDeadPods(int n, vector<vector<int>> connections, vector<vector<int>> queries) {
    vector<int> res;
    DSU uf(n);
    
    for (auto& conn: connections) {
        uf.join(conn[0], conn[1]);
    }
    
    unordered_map<int, set<int>> regions;
    for (int i = 1; i <= n; ++i) {
        regions[uf.find(i)].insert(i);
    }
    
    vector<bool> alive(n + 1, true);
    
    // ----
    
    for (auto& q: queries) {
        int qid = q[0];
        int podId = q[1];
        int parent = uf.find(podId);
        
        if (qid == 2) {
            alive[podId] = false;
            if (regions[parent].find(podId) != regions[parent].end()) {
                regions[parent].erase(podId);
            }
        }
        else {
            if (alive[podId]) {
                res.push_back(podId);
            }
            else {
                int smallestAlive = -1;
                if (!regions[parent].empty()) {
                    smallestAlive = *regions[parent].begin();
                }
                res.push_back(smallestAlive);
            }
        }
    }
    
    return res;
}
```

---
