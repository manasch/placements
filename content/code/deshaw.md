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


[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 19/11/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 4 sections:

1. Coding (20 min)
2. Coding (30 min)
3. Aptitude
4. Technical

Totally around 95 min.

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

## Round 2

> 25/11/23

Was a technical round.

- Introduce yourself
- Projects discussions
- [Probabily Puzzle](https://www.geeksforgeeks.org/generate-0-1-25-75-probability/)
- [Delete and Earn](https://leetcode.com/problems/delete-and-earn/)
- Given a python code, how would you decide if it is indented properly or not, write code to check if a given python code is indented correctly.

---

## Round 3

> 26/11/23

Was technical and scenario based.

- Interests, Introduction
- How does google autofill work, how would you go about implementing such a system.
- There are millions of records in an excel sheet, and different columns, a particular cell for some employee could be color coded due to certain conditions, similarly another cell could be differently colored due to other conditions. How would you optimize this process in the backend and send the colors to the front end.
- Ludo game with n players, at max 4 players can play at once, not necessary for all 4 to play a game, find out the minimum number of games required such that each player plays every other player atleast once.
- Difference between a get and post request, if you give a html page with a button that sends some post request when clicked that could modify the database by mistake and do not want them to make any changes, how would you handle this.

---
