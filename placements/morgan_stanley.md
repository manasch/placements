# [Morgan Stanley](http://www.morganstanley.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 8 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE       | Internship |
|--------|-----------|------------|
| Base   | --        | --         |
| Stocks | --        | --         |
| Bonus  | --        | --         |
| CTC    | 29.48 LPA | 87000      |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 17/09/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 3 sections and a total of 100 min.

1. Automata Fix (7) - 20min - (A debugging section, debug code such that it passes all test cases.)
2. Quantitative and Logical Aptitude (10) - 20min
3. Coding (3) - 60min

### Coding Questions

1. **Longest Common Prefix**: Given an array of names, find the longest common prefix of all the names.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
string solve(vector<string>& names, int n) {
	if (n == 0) {
		return "";
	}
	if (n == 1) {
		return names[0];
	}
	
	sort(names.begin(), names.end());
	string min_string = names.front().size() < names.back().size() ? names.front() : names.back();
	int min_length = min_string.size();
	
	int i = 0;
	string res = "";
	while (i < min_length && names.front()[i] == names.back()[i]) {
		res += min_string[i];
		++i;
	}
	return res;
}

int main()
{
	int n;
	cin >> n;
	vector<string> names(n);
	for (int i = 0; i < n; ++i) {
		cin >> names[i];
        transform(names[i].begin(), names[i].end(), names[i].begin(), [](unsigned char c) {return tolower(c);})
	}
	
	string res = solve(names, n);
	cout << res << endl;
	return 0;
}
```

- [GFG](https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/)

---

2. **Max Substring Length**: Given a number as string, find the largest length of a substring of size 2k such that the sum of left k digits is equal to the sum of the right k digits.

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
num = input()
n = len(num)

maxLen = 0

for i in range(n - 1):
    l = i
    r = i + 1

    leftSum = 0
    rightSum = 0
    while (l >=0 and r < n):
        leftSum += int(num[l])
        rightSum += int(num[r])
        if leftSum == rightSum:
            maxLen = max(maxLen, r - l + 1)
        l -= 1
        r += 1

print(maxLen)
```

---
3. **Number of Different Plants**: Given a 2D matrix of 0's and 1's, find the different number plants that exist. In the cell, if a plant exists, it is marked as 1 otherwise 0.
    
    The plants that are connected 4-sided are of the same type, whereas the plants that are connected diagonally are considered different plants. Hence given these conditions, find the total number of different plants.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(vector<vector<int>>& matrix, int m, int n) {
	int count = 0;
	set<pair<int, int>> visited;
	
	auto bfs = [&] (auto self, int i, int j) {
		if (min(i, j) < 0 || i >= m || j >= n) {
			return;
		}
		if (matrix[i][j] == 0 || visited.find({i, j}) != visited.end()) {
			return;
		}
		visited.insert({i, j});
		self(self, i, j + 1);
		self(self, i + 1, j);
		self(self, i, j - 1);
		self(self, i - 1, j);
	};
	
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (matrix[i][j] == 1 && visited.find({i, j}) == visited.end()) {
				bfs(bfs, i, j);
				++count;
			}
		}
	}
	
	return count;
}

int main()
{
	int n, m;
	cin >> n >> m;
	vector<vector<int>> graph(n, vector<int>(m, 0));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> graph[i][j];
		}
	}
	
	int ans = solve(graph, n, m);
	cout << ans << endl;
	return 0;
}
```

- This is exactly [LC#200](https://leetcode.com/problems/number-of-islands) but worded differently.

---
