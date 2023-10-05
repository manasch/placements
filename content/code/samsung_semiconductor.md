# [Samsung Semiconductor India Research](https://news.samsung.com/in/tag/samsung-semiconductor-india-research)

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

- No Backlogs

### Compensation

|        | FTE | Internship |
|--------|-----|------------|
| Base   | --  | 50K        |
| Stocks | --  | --         |
| Bonus  | --  | --         |
| CTC    | --  | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 05/10/23

[comment]: # (Summary of the sections and experience below this comment.)

One section with 3 coding questions for 70 min.

### Coding Questions

1. **Alternate Levels**: Given the root of a binary tree, return the sum of all the nodes in the alternate levels of a binary tree starting from the root. If the root is null then return 0.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(TreeNode *root) {
    if (root == nullptr) {
        return 0;
    }
    int res = 0;
    int level = 0;
    queue<TreeNode *> q;

    q.push(root);
    while (!q.empty()) {
        int n = q.size();
        while (n--) {
            TreeNode *t = q.front();
            q.pop();

            if (level % 0 == 0) {
                res += t->data;
            }
            if (t->left) {
                q.push(t->left);
            }
            if (t->right) {
                q.push(t->right);
            }
        }
        ++level;
    }

    return res;
}
```

---

2. **Number of Components**: Given an m*n binary matrix, a connected component is a set of 1's that can be reached 8-directionally. Return the number of connected components.

> This is basically Number of Islands on LeetCode but 8-dxns

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(int **graph, int m, int n) {
    set<pair<int, int>> visited;

    auto dfs = [&] (auto self, int i, int j) {
        if (min(i, j) < 0 || i >= m || j >= n) {
            return;
        }
        if (visited.find({i, j}) != visited.end() || graph[i][j] == 0) {
            return;
        }
        visited.insert({i, j});

        self(self, i, j + 1);
        self(self, i + 1, j);
        self(self, i, j - 1);
        self(self, i - 1, j);

        self(self, i - 1, j + 1);
        self(self, i - 1, j - 1);
        self(self, i + 1, j + 1);
        self(self, i + 1, j - 1);
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (visited.find({i, j}) == visited.end() && graph[i][j] != 0) {
                dfs(dfs, i, j);
                ++res;
            }
        }
    }
    return res;
}
```

---

3. **Next Palindrome**: Given a number as a string, find the first number greater than the current one that is a palindrome.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
void helper(char *num, int n, bool *isPalin) {
    int l = 0;
    int r = n - 1;
    int p, t, oldr;
    char c;

    while (l < r) {
        if (num[l] != num[r]) {
            oldr = num[r];
            num[r] = num[l];

            if (oldr > num[l]) {
                t = r - 1;
                while (t > 0) {
                    c = num[t];
                    p = atoi(c);
                    ++p;

                    if (p < 10) {
                        num[t] = p + '0';
                        break;
                    }
                    else {
                        num[t] = '0';
                    }
                    --t;
                }
            }
        }
        ++l;
        --r;
    }

    if (l >= r) {
        isPalin = true;
    }
}

int solve(char *num) {
    int len = 0;
    while (num[len] != '\0') {
        ++len;
    }

    bool isPalin = false;
    while (!isPalin) {
        helper(num, len, &isPalin);
    }
    return num;
}
```

> Not sure if this would pass hidden cases, did pass the visible ones.

---
