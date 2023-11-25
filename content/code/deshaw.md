# [DE Shaw](https://www.deshaw.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 7 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|                     | FTE                   | Internship |
|---------------------|-----------------------|------------|
| Base                | 18,00,000             | 1,50,000   |
| Variable            | 2,00,000 - 4,00,000   | --         |
| Joining Bonus       | 3,00,000              | --         |
| Non Cash Benefits   | 5,00,000              | --         |
| Relocation          | 2,00,000              | --         |
| Long Term Incentive | 20,00,000             | --         |
| CTC                 | 50,00,000 - 52,00,000 | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 19/11/23

[comment]: # (Summary of the sections and experience below this comment.)

### Coding Questions

1. **Min-Max Difference**: Given a string of characters (only smaller case), find out the number of minimum number of characters to remove such that the difference between the max frequency of chars and the min frequency of chars is `m` which is given.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(string s, int m) {
	int res = 0;
	unordered_map<char, int> freq;
	vector<int> arr;

	for (char ch: s) {
		++freq[ch];
	}

	for (auto& [k, v]: freq) {
		arr.push_back(v);
	}

	sort(arr.begin(), arr.end());

	int r = arr.size() - 1;
	int l = 0;
	while (l < r && arr[r] - arr[l] > m) {
		int a = arr[r - 1] - arr[l]; // Removing the max
		int b = arr[r] - arr[l + 1]; // Removing the min

		if (a < b) {
			res += arr[r];
			--r;
		}
		else {
			res += arr[l];
			++l;
		}
	}

	return res;
}

```

---

2. **Greatest String**: You are given a string as input (only consisting of smaller case characters), you are also given two empty strings `pre` and `post`.

    The following operations can be performed:

    1. The prefix of the input string can be pushed to the end of the `pre` string.
    2. The postfix of the `pre` string can be pushed to the `post` string.

    Using these operations, create the lexicographically string possible.

    Example:
    ```md
    Input: bcdadb

    | Input  | Pre   | Post   |
    |--------|-------|--------|
    | bcdadb | -     | -      |
    | cdadb  | b     | -      |
    | dadb   | bc    | -      |
    | adb    | bcd   | -      |
    | db     | bcda  | -      |
    | db     | bcd   | a      |
    | b      | bcdd  | a      |
    | -      | bcddb | a      |
    | -      | bcdd  | ab     |
    | -      | bcd   | abd    |
    | -      | bc    | abdd   |
    | -      | b     | abddc  |
    | -      | -     | abddcb |

    Output: abddcb
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
string solve(string s) {
    string res;
    stack<pair<char, int>> st;
    vector<bool> better(s.size(), false);
    
    for (int i = s.size() - 1; i >= 0; --i) {
        for (int j = i + 1; j < s.size(); ++j) {
            if (s[j] < s[i]) {
                better[i] = true;
                break;
            }
        }
    }
    
    for (int i = 0; i < s.size(); ++i) {
        st.push({s[i], i});
        while (!st.empty() && !better[st.top().second]) {
            res.push_back(st.top().first);
            st.pop();
        }
    }
    while (!st.empty()) {
        res += st.top().first;
        st.pop();
    }
    return res;
}

```

---
