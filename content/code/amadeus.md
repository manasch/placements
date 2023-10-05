# [Amadeus](https://amadeus.com/en)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff  |
|-------|---------|
| X     | 80%     |
| XII   | 80%     |
| UG    | 7.5 GPA |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|                      | FTE       | Internship |
|----------------------|-----------|------------|
| Base                 | 10,00,000 | --         |
| Allowance (One Time) | 1,50,000  | --         |
| Bonus                | 85,464    | --         |
| Insurance Benefits   | 26,754    | --         |
| CTC                  | 12,62,218 | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 05/10/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 2 sections and of 31 Questions and 90 min were given.
1. Technical MCQ (29)
2. Coding (2)

### Coding Questions

1. **Number of Sale Dayes**: A shop operates for N days, an array of size N is given where each day the value can either be 1, 0, -1.

    If v = 1, then the shopkeeper restocks his inventory and discard his old one (if any). He can't sell anything on that day.
    If v = 0, then the shopkeeper can sell the items on that day (if he has any items).
    If v = -1, then the shopkeeper will return back all the item in the shop back to the inventory and can't sell until he restocks.

    Find the maximum number of days the shop has items on sale for one lot of items. (lot refers to the items he gets upon a restock)

    Ex:
    ```
    4
    1 1 0 0

    Output: 2
    The shop can be on sale for a max of 2 days on 1 lot.

    5
    1 0 -1 0 0

    Output: 1
    The shop has nothing in inventory after 3rd day.

    5
    1 0 0 1 0

    Output: 2
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(vector<int>& shop) {
    int n = shop.size();
    bool canSell = false;
    int res = 0;
    int cur = 0;

    for (int x: shop) {
        if (canSell) {
            if (x == 0) {
                ++cur;
            }
            else {
                res = max(res, cur);
                cur = 0;
                if (x == -1) {
                    canSell = false;
                }
            }
        }
        else {
            if (x == 1) {
                canSell = true;
            }
        }
    }
    return res;
}
```

---

2. **Free Intervals**: A ground is occupied during certain intervals, return an array of intervals when the grouns is free to use. [0, 1e9] is the range of hours.

    Given
    - N: Number of intervals when ground is in use.
    - L: An array of size N which represents the start time of the intervals.
    - R: An array of size N which represents the end time of the intervals.

    No two intervals overlap, and `R[i] < L[i + 1]` for `0 < i < UL`.

    If no intervals exist, return `[[-1, -1]]`

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
vector<vector<int>> solve(vector<int> R, vector<int> L, int N) {
    vector<vector<int>> res;
    int end = 1e9;

    for (int i = 0; i < N; ++i) {
        if (i == 0) {
            if (L[i] == 0) {
                res.push_back({0, L[i]});
            }
        }
        else if (i == N - 1) {
            if (R[i] != end) {
                res.push_back({R[i], end});
            }
        }
        else {
            if (R[i - 1] < L[i]) {
                res.push_back({R[i - 1], L[i]});
            }
        }
    }

    if (res.size() > 0) {
        return res;
    }
    return vector<vector<int>> {{-1, -1}};
}
```

---

## Round 1

> 05/10/23

[comment]: # (Summary of the sections and experience below this comment.)

An SHL assessment of 2 sections.
1. Aptitude (19)
2. Verbal (25)

---
