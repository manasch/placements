# [Eli Lilly](https://www.lilly.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

|Study|Cutoff|
|-----|------|
|X|%|
|XII|%|
|UG|GPA|

[comment]: # (Any other details go under this. This is a comment)

### Compensation

||FTE|Internship|
|--|-----|------|
|Base|1100000|30000|
|Stocks|--|--|
|Bonus|--|--|
|CTC|--|--|

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 14/09/23

[comment]: # (Summary of the sections and experience below this comment.)

There were totally 4 sections and it was 2 hours. The sections were not times, could allocate how much ever time required for any section.

1. Reasoning (24)
2. Programming (8) - Basically all were SQL
3. Quantitative (23)
4. Coding (3) - Everyone got different questions.

### Coding Questions

1. **War Ships**: Given two inputs, layers and modulus. Return the total number of ships required mod the modulus.
Each ship is assigned a value V and the first layer has 1 ship with value 2. For each ship, the number of ships in the layer after are decided by the value V for that ship. The number of ships in the next layer for that ship is: `[V * V + 1] % M` where M is the modulus and the values for those ships will be ranging from `[0, ([V * V + 1] % M) - 1]`.

Ex: L = 2, M = 3
Layer 1: 1 ship with V = 2
Layer 2: 2 ships with V = [0, 1] because [2 * 2 + 1] % 3 = 2.

Output would be 0 as total number of ships is 3 and 3 % 3 is 0.

[comment]: # (Add any resources or links or code to this question under this comment.)

2. **Stealing Window**: A thief is trying to steal from a bank. The bank has N guards and each guard will guard the place for a certain interval. The bank will be open for T minutes. The thief needs X minutes to complete the heist, and it can be split, not all the X mins need to be done at once. Given the intervals at which each guard will be in front of the bank. Determine whether it is possible for the thief to perform the heist.

Input: N, T, X, Intervals = [start, end, start, end, start, end...]

> Find the available time between the intervals and return "Possible Z" or "Impossible Z" where Z is the free time between the intervals that the theif has to perform the heist.

[comment]: # (Add any resources or links or code to this question under this comment.)

3. **Aron's Gift**: Aron shows preference to two characters C1 and C2. He gives a string consisting of just these two characters. Given the string length and the two characters he likes. Return the number of strings (substrings) that are possible such that it starts with C1 and ends with C2.

Inputs:
- N - Length of string
- C1 - Character 1
- C2 - Character 2
- S - String

Ex:
N - 3
C1 - x, C2 - y
S = xxy

Output: 2 - ["xxy", "xy"]

N - 2
C1 - a, C2 - b
S = ab

Output: 1 - ["ab"]

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int solve(int n, char c1, char c2, string s) {
    int countC1 = 0;
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == c1) {
            ++countC1;
        }
        else {
            res += countC1;
        }
    }

    return res;
}

```

---
