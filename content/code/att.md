# [AT&T](https://www.att.com/)

## Details

### Job Status

Internship + Performance Based Conversion

### Criteria

| Study | Cutoff  |
|-------|---------|
| X     | 80%     |
| XII   | 80%     |
| UG    | 7.5 GPA |

[comment]: # (Any other details go under this. This is a comment)

- 8.5+ GPA were selected

### Compensation

|        | FTE              | Internship |
|--------|------------------|------------|
| Base   | --               | 45356      |
| Stocks | --               | --         |
| Bonus  | --               | --         |
| CTC    | Minimum of 16LPA | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 16/11/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 3 sections:

1. Technical MCQ (35) - 35 Min - 35 Marks
2. Aptitude MCQ (10) - 10 Min - 10 Marks
3. Coding (5) - 45 Min - 50 Marks

### Coding Questions

1. **Binary Search**: Find the target element in a sorted array. Return -1 if not found.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(vector<int>& arr, int target) {
    int n = arr.size();
    int beg = 0; int end = n - 1;
    int mid;

    while (l <= r) {
        mid = beg + ((end - beg) >> 1);
        if (arr[mid] > target) {
            end = mid - 1;
        }
        else if (arr[mid] < target) {
            beg = mid + 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}
```

---

2. **String Matching**: Find out whether the target string exists in the given sentence.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
bool solve(string s, string p) {
    return (s.find(p) != string::npos);
}

int main() {
    vector<string> inp;
    string temp;

    while (cin >> temp) {
        inp.push_back(temp);
    }

    string sentence, word;

    for (int i = 0; i < inp.size(); ++i) {
        if (i == inp.size() - 1) {
            word = inp[i];
        }
        else {
            sentence += inp[i] + " ";
        }
    }

    cout << solve(sentence, word);
    return 0;
}
```

---

3. **Increasing Sum Sequence**: The given input is a string of digits, from the 3rd digit onwards, it should be the sum of the previous 2 digits.

    Find out whether the given string is an ISS or not.

> Basically Fibonacci

[comment]: # (Add any resources or links or code to this question under this comment.)

---

4. **[ongest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)**

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int lcs(string a, string b) {
    int n = a.size();
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            }
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n][n];
}

int solve(string s) {
    string t = s;
    reverse(t.begin(), t.end());
    return lcs(s, t);
}
```

```cpp
int solve(string s) {
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, -1));

    auto dfs = [&] (auto self, int i, int j) {
        if (i < 0 || j >= n) {
            return 0;
        }
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        if (s[i] == s[j]) {
            dp[i][j] = (i == j) 1 : 2 + self(self, i - 1, j + 1);
        }
        else {
            dp[i][j] = max(self(self, i - 1, j), self(self, i, j + 1));
        }
        return dp[i][j];
    };

    int res = 0;
    for (int i = 0; i < n; ++i) {
        res = max(dfs(dfs, i, i));
        res = max(dfs(dfs, i, i + 1));
    }
    return res;
}
```

---

5. **Longest Continous Increasing Subarray**: Given an array, find out the length of the longest increasing subarray.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(vector<int>& arr) {
    int n = arr.size();
    int res = 1;
    int cur = 1;

    for (int i = 1; i < n; ++i) {
        if (arr[i] > arr[i - 1]) {
            ++cur;
        }
        else {
            res = max(res, cur);
            cur = 1;
        }
    }
    res = max(res, cur);
    return res;
}
```

---
