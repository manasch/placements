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

1. **Sum of total waiting time**: There are N clients who have ordered N handmade items. The K-th client ordered exactly one item that takes T[k] hours to make. There is only one employee who makes items for clients, and they work in the following manner:
    - spend one hour making the first item;
    - if the item is finished, the employee delivers it to the client immediately;
    - if the item is not finished, they put it after the N-th item for further work;
    - the employee starts making the next item.

For example for T = [3, 1, 2], the employee spends 6 hours making the items in the following order: [1, 2, 3, 1, 3, 1]. The first client waited 6 hours for their item, the second client received their item after 2 hours and the third client after 5 hours. What is the total time that clients need to wait for all ordered items? For the above example, the answer is 6 + 2 + 5 = 13.

As the result may be large, return its last nine digits without leading zeros (in other words, return the result modulo 10^9)

Examples:

1. Given T = [3, 1, 2], the function should return 13 as explained above.

2. Given T = [1, 2, 3, 4], the function should return 24. The employee prepares the itesm in the following order: 1, 2, 3, 4, 2, 3, 4, 3, 4, 4. The first client waited for 1 hor, the second client for 5 hors, the third client for 8 hors, and the fourth client for 10 hors. The total waiting time for all clients if 1 + 5 + 8 + 10 = 24 hours.

3. Given T = [7, 7, 7], the function should return 60.

4. Given T = [10000], the function should return 10000.

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

2. **Max tiles coverage**: There is an array A of N integers and three tiles. Each tile can cover two neighbouring numbers from the array but cannot interesct with another file. It also cannot be placed outside the array, even partially.

Write a function:
    `int solution(vector<int> &A);`

that, given an array A of N integers, returns the maximum sum of numbers that can be covered using at most three tiles.

Examples:

1. Given A = [2, 3, 5, 2, 3, 4, 6, 4, 1], the function should return 25. There is only one optimal placement of tiles: (3, 5), (3, 4), (6, 4).

2. Given A = [1, 5, 3, 2, 6, 6, 10, 4, 7, 2, 1], the function should return 35. One of the three optimal placements of tiles is (5, 3), (6, 10), (4, 7).

3. Given A = [1, 2, 3, 3, 2], the function should return 10. There is one optimal placement of tiles: (2, 3), (3, 2). Only two tiles can by used because A is too small to contain another one.

4. Given A = [5, 10, 3], the function should return 15. Only one tile can be used.

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

```cpp
int solution(vector<int> arr)
{
    vector<vector<int>> dp(arr.size() + 2, vector<int> (4, 0));
    int max_ele = 0;
    for(int i = 2; i < dp.size(); i++)
    {
        for(int j = 1; j < dp[0].size(); j++)
        {
            if(i >= 2 * j)
            {
                dp[i][j] = max(dp[i - 2][j - 1] + arr[i - 2], dp[i - 1][j]);
                if(dp[i][j] > max_ele)
                {
                    max_ele = dp[i][j];
                }
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return max_ele;
}
```
- Bottom-up DP

---
