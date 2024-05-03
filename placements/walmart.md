# [Walmart](https://www.walmart.com)

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


[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 15/11/23

[comment]: # (Summary of the sections and experience below this comment.)

2 Sections

1. MCQ (Technical)
2. Coding (2)

### Coding Questions

1. **Mode Selection**: You are given the scores of n students, a company wants to select students who have scored the mode of the n students. Return the number of students to reject.

    Example:
    ```
    4
    2 2 3 4

    Output:
    2

    The mode is 2 and hence the other students who did not score 2 are rejected

    6
    3 4 3 4 5 6

    Output:
    4

    The mode is either 3 or 4, hence you can reject (4 4 5 6) or (3 3 5 6) making it 4 in total.
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(vector<int>& scores) {
    int n = scores.size();
    sort(scores.begin(), scored.end());

    int mode = 1;
    int current = 1;
    for (int i = 1; i < n; ++i) {
        if (scores[i] == scores[i - 1]) {
            ++current;
        }
        else {
            mode = max(mode, current);
            current = 1;
        }
    }
    mode = max(mode, current);

    return n - mode;
}
```

---

2. **Array By 5**: Given an `nxm` array, replace all the elements in it with the closest number that is divisible by 5.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
void solve(vector<vector<int>>& arr) {
    int n = arr.size();
    int m = arr[0].size();

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int num = arr[i][j];
            int q = num / 5;
            int lower = 5 * q;
            int higher = lower + 5;
            bool isLower = (num - lower) < (higher - num) ? true : false;

            arr[i][j] = isLower ? lower : higher;
        }
    }
}
```

---
