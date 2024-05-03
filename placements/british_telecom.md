# [British Telecom](https://www.bt.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | GPA    |

[comment]: # (Any other details go under this. This is a comment)


[comment]: # (Details about the rounds go under this comment.)

## Round 1 - Coding Round

> 19/09/23

[comment]: # (Summary of the sections and experience below this comment.)

A total of 13 questions. Time - 120 min.
1. MCQ (10) - Technical - (KMP and N-Queens TC was asked)
2. Coding (3) - 1 SQL

### Coding Questions

1. **Maximum Friendship Power**: There are N Cities and M Bi-Directional Roads. An array A of size N consists of the number of people in each group (there are N groups). A city is connected to another city if it can be reached by the roads. A set of connected cities form a kingdom.

    Given these values, generate a permutation array B (of size N) which assigns the groups to the cities respectively such that the maximum friendship power can be formed. Friendship power is determined by the number of unique connections among X people, i.e. (X * (X - 1)) / 2.
    
    Since this number can be large, give the answer % *mod_value (A number was given which I forgot)*. (Assume 1-indexing).
    
    Example:
    
    N = 4\
    M = [[1,3], [2,4]]\
    A = [6,2,1,3]
    
    Output: 39 (2 kingdoms 36 + 3)

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(int n, int m, vector<vector<int>>& roads, vector<int>& a) {
    unordered_map<int, vector<int>> adj;
    for (auto road: roads) {
        adj[road[0]].push_back(road[1]);
        adj[road[1]].push_back(road[0]);
    }

    priority_queue<int> groups(a.begin(), a.end());
    priority_queue<int> kingdoms;
    unordered_set<int> visited;
    
    auto dfs = [&] (auto self, int src, int& count) {
        if (visited.find(src) != visited.end()) {
            return;
        }
        visited.insert(src);
        ++count;
        
        for (int neigh: adj[src]) {
            if (visited.find(neigh) == visited.end()) {
                self(self, neigh, count);
            }
        }
    };
    
    int count;
    for (int i = 1; i <= n; ++i) {
        count = 0;
        dfs(dfs, i, count);
        if (count > 0) {
            kingdoms.push(count);
        }
    }
    
    int mod = 1e9 + 7; // Just taking some random modulus as I don't remember what they gave.
    int res = 0;
    int currentSum = 0;
    int currentKingdomCount;
    while (!kingdoms.empty()) {
        currentKingdomCount = kingdoms.top();
        kingdoms.pop();
        
        currentSum = 0;
        while (currentKingdomCount--) {
            currentSum += groups.top();
            groups.pop();
        }
        res += ((currentSum) * (currentSum - 1) / 2) % mod;
    }
    return res;
}
```
- This passed half the test cases, IDK why :(

---

2. **Number in a Range**: Three numbers L, R, K are given, where [L, R] determine a range of numbers to consider. Find the K'th number in the range such that the pattern 101 occurs anywhere in the binary representation of the number. If the K'th number doesn't exist, return -1.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
bool containsPattern(int n) {
    int p = 5; // 5 in binary is 101, the pattern to match.
    int t = 7; // 7 in binary is 111, when anded with this, will give the group of 3 bits to check.
    
    while (p <= n) {
        if ((n & t) == p) {
            return true;
        }
        p <<= 1;
        t <<= 1;
    }
    return false;
}

int solve(int l, int r, int k) {
    int res = -1;
    for (int i = l; i <= r; ++i) {
        if (containsPattern(i)) {
            --k;
            cout << i << " ";
        }
        if (k == 0) {
            res = i;
            break;
        }
    }
    return res;
}
```

- ~~This TLE'd, some tricky math for optimization maybe~~ Digit DP + Binary Search.
- [Coding Ninjas](https://www.codingninjas.com/studio/problems/k-th-perfect-number-in-range_2569269)

---

### SQL

3. **International and Domestic Flights**: Given a table airports consisting of columns (id, code, country) where code is the shortform for a state. Return the total number of international flights and domestic flights.

    Example: 
    
    | id | code | country |
    |----|------|---------|
    | 1  | CAL  | USA     |
    | 2  | TEX  | USA     |
    | 3  | FLO  | USA     |
    | 4  | ALA  | USA     |
    | 5  | BER  | GER     |
    | 6  | LUX  | BEL     |
    
    Output: 
    | International | Domestic |
    |---------------|----------|
    | 9             | 6        |

[comment]: # (Add any resources or links or code to this question under this comment.)

```sql
select (
    select round(count(*) / 2, 0)
    from airports a1 join airports a2
    where a1.code != a2.code and a1.country != a2.country
) as "International", (
    select round(count(*) / 2, 0)
    from airports a1 join airports a2
    where a1.code != a2.code and a1.country = a2.country
) as "Domestic";
```

---

## Round 2 - Interview

- About yourself.
- Resume based, projects discussions.
- 3 DSA and 1 Pattern printing
    - Given n, print the pattern as 1, 2, 3 ... n ... 3, 2, 1
    - Detect a cycle in a linked list.
    - Longest occurances of 1's in a binary array, same but in a circular binary array.
    - Given an array of integers, replace each element with the next greatest element from the array to its right. (Daily Temperatures on LC)

---
