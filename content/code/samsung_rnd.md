# [Samsung Research Institute](https://research.samsung.com/)

## Details

### Job Status

Internship Only

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 7 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE | Internship |
|--------|-----|------------|
| Base   | --  | 50000      |
| Stocks | --  | --         |
| Bonus  | --  | --         |
| CTC    | --  | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 18/10/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 3 coding questions to be solved in 80 min, everyone got 3 questions from a pool of questions.

### Coding Questions

1. **Christmas Gifts**: There are N chocolates and M toys, a gift box can have either X chocolates and Y toys or X toys and Y chocolates.

    Find the maximum number of gift boxes that can be made.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(int n, int m, int x, int y) {
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));

    auto dfs = [&] (auto self, int i, int j) {
        if (min(i, j) < 0) {
            return -1;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        int left = self(self, i - x, j - y);
        int right = self(self, i - y, j - x);

        return dp[i][j] = 1 + max(right, left);
    };
    
    return dfs(dfs, n, m);
}
```

---

2. **Hamiltonian Circuits**: Given an undirected graph, return the total number of unique hamiltonian circuits.

    > Note: An hamiltonian circuit is a path in which each node in the graph is visited once except for the source node which is visited twice.

[comment]: # (Add any resources or links or code to this question under this comment.)

- [GFG](https://www.geeksforgeeks.org/print-all-hamiltonian-cycles-in-an-undirected-graph/)

---

3. **Worms**: Given some number of worms and some number of interactions amongst the worms, figure out whether these interactions are valid or not.

    A worm can be a male or female. A valid interaction is when a male worm interacts with the female worm and vice versa.

    For the given set of interactions, figure out if it is a valid set of interactions or an invalid set of interactions.

    Ex:
    ```md
    3 (worms) 3 (interactions)
    1 2
    2 3
    1 3

    This is invalid as 1 interacts with 2 and 3 but 2 interacts with 3, there is no possible combination of genders where this is valid.
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

---
