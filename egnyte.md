# [Egnyte](https://www.egnyte.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

|Study|Cutoff|
|-----|------|
|X|%|
|XII|%|
|UG|7.5 GPA|

[comment]: # (Any other details go under this. This is a comment)

### Compensation

||FTE|Internship|
|--|-----|------|
|Base|--|50000|
|Stocks|--|--|
|Bonus|--|--|
|CTC|1400000 - 1500000|--|

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 19/08/23

[comment]: # (Summary of the sections and experience below this comment.)
There was only one coding section with 2 questions, everyone had a combination of 2 from a pool of questions.

### Coding Questions

1. **Sum of total waiting time**: ***REMOVED***
    - 
    - 
    - 
    - 





Examples:

1. 

2. 

3. 

4. 

> Create a queue, push all tasks to it, have a counter that is always increasing. Pop the queue and if after decrementing the value becomes 0, add the current counter val to the total variable with mod, else push it to the back of the queue. Repeat till the queue is empty.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
#include <queue>
#include <vector>
using namespace std;

int solution(vector<int> arr) {
    queue<int> q;
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        q.push(arr[i]);
    }

    int hours = 1;
    int modulo = 1e9;
    int total = 0;

    while (!q.empty()) {
        int task = q.front();
        --task;
        q.pop();
        if (task == 0) {
            total = (total + hours) % modulo;
        }
        else {
            q.push(task);
        }
        ++hours;
    }
    return total;
}
```

2. **Max tiles coverage**: ***REMOVED***


    `int solution(vector<int> &A);`



Examples:

1. 

2. 

3. 

4. 

> Create another array of sums of it's adjacent neighbour, perform a 2D House-Robber approach to find the best possible sum of values covered by tiles.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
void dfs(vector<int>& tileSum, size_t idx, int& largestSum, int sum, int tiles) {
    if (tiles == 0) {
        largestSum = max(largestSum, sum);
        return;
    }
    if (idx >= tileSum.size()) {
        return;
    }
    sum += tileSum[idx];
    // cout << sum << endl;
    for (size_t i = idx + 2; i <= tileSum.size() + 2; ++i) {
        dfs(tileSum, i, largestSum, sum, tiles - 1);
    }
}

int solution(vector<int> &A) {
    // Implement your solution here
    int n = A.size();
    int tiles;
    if (n >= 6) {
        tiles = 3;
    }
    else if (n >= 4 && n < 6) {
        tiles = 2;
    }
    else {
        tiles = 1;
    }
    vector<int> tileSum;
    for (int i = 0; i < n - 1; ++i) {
        tileSum.push_back(A[i] + A[i + 1]);
    }
    int largestSum = 0;
    for (size_t i = 0; i < tileSum.size(); ++i) {
        dfs(tileSum, i, largestSum, 0, tiles);
    }
    return largestSum;
}
```
- This would most likely TLE for large test cases. Didn't know how to use 2d DP.
---
