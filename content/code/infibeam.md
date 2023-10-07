# [Infibeam](www.ia.ooo)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | 80%    |
| XII   | 80%    |
| UG    | 8GPA   |

[comment]: # (Any other details go under this. This is a comment)

- There was another cut off, probably 8.5 GPA

### Compensation

|        | FTE           | Internship |
|--------|---------------|------------|
| Base   |               | 20,000     |
| Stocks | --            | --         |
| Bonus  | 2L (One Time) | --         |
| CTC    | 10 + 2L       | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 07/10/23

[comment]: # (Summary of the sections and experience below this comment.)

There was only 1 section, 22 questions of which 2 were coding, a total of 1h45m was given to complete the test.

### Coding Questions

1. **Height of a tree**: Given a binary tree, find the height of the tree by skipping the nodes that have odd-valued data.
    - The height of an empty tree is *0*
    - The height of a tree with just the root is also *0*.
    - If all the nodes are odd-valued, then the height is *0*.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(Node *root) {
    int res = 0;

    auto dfs = [&] (auto self, Node *node, int height) {
        if (node == nullptr) {
            res = max(res, height);
            return;
        }
        if (node->data % 2 == 0) {
            ++height;
        }
        self(self, node->left, height);
        self(self, node->right, height);
    };

    dfs(dfs, root, 0);
    return max(res - 1, 0);
}
```

---

2. **[Word Search](https://leetcode.com/problems/word-search/)**

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
void solve(vector<vector<char>>& board, string word) {
    int m = board.size();
    int n = board[0].size();
    bool containsWord = false;

    visited<pair<int, int>> visited;

    auto bfs = [&] (auto self, int i, int j, int idx) {
        if (min(i, j) < 0 || i >= m || j >= n || containsWord) {
            return;
        }
        if (visited.find({i, j}) != visited.end()) {
            return;
        }
        if (idx == word.size()) {
            containsWord = true;
            return;
        }
        visited.insert({i, j});
        if (board[i][j] == word[idx]) {
            self(self, i, j + 1);
            self(self, i, j - 1);
            self(self, i + 1, j);
            self(self, i - 1, j);
        }
        visited.erase({i, j});
    };

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            bfs(bfs, i, j, 0);
            if (containsWord) {
                break;
            }
        }
        if (containsWord) {
            break;
        }
    }
    cout << boolalpha << res << endl;
}
```

---
