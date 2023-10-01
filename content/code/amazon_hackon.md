# [Amazon HackOn 2023](https://unstop.com/competitions/hackon-with-amazon-season-3-amazon-729950)

## Details

### Job Status

Hackathon. Winners offered internships/FTE and prize money.

### Criteria

- 6.5 CGPA Engineering students
- 2-4 members per team

### Prizes

- Winner - INR 1,00,000
- 1st runner-up - INR 75,000
- 2nd runner-up - INR 50,000
- Mentorship for the Top 8 teams
- SWAG for the Top 8 teams  
- The Titan - Top 50 coders - Exciting Prizes
- The Wonder Woman - Top 5 Female Coders - Exciting Prizes
- The Trailblazer - Top 5 Fastest Coders - Exciting Prizes
- The Zen Master - Top 5 Cleanest Coders - Exciting Prizes

## Round 1

> 28/09/2023

Every member of team had to solve 20 MCQs in 20 minutes. The questions were based on DSA and coding fundamentals.

## Round 2 (Coding)

> 29/09/2023

Every member of team had to solve 2 coding questions in 90 minutes. Problems were random and of various difficulty levels. As a team of 3, we had to solve 6 questions in total mentioned below.

1. Given `n` strings, determine the pair with the max value product. `n` is upto 10^6 and each string has max length of 20. The strings can contain alphanumeric characters. If a string contains any numeric character, it's value is the integer concatenation of all numeric characters. Otherwise, it is the length of the string.

> Convert all strings to their values and find the two biggest values. Multiply them to get the answer.

Example:

```
3
abc a01 a42

Answer: Values are [3, 1, 42]. Max product is 42 * 3 = 126
```

```python
n = int(input())
s = input().split()
a = []
for i in s:
    if i.isnumeric():
        a.append(int(i))
    else:
        value = 0
        has_numeric = False
        for j in i:
            if j.isnumeric():
                value = value * 10 + int(j)
                has_numeric = True
        if not has_numeric:
          value = len(i)
        a.append(value)
a.sort()
print(a[-1] * a[-2])
```

2. Find the longest subsequence in an array such that each element is 3 times more than the previous element. `n` is upto 100 and `a[i]` is upto 2000.

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

void solve() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i)
        std::cin >> a[i];
    
    std::vector<int> dp(n + 1);

    for (int i = 1; i <= n; ++i) {
        int max = 0;
        for (int j = 1; j < i; ++j) {
            if (a[j - 1] * 3 == a[i - 1])
                max = std::max(max, dp[j]);
        }
        dp[i] = 1 + max;
    }

    std::cout << *std::max_element(dp.begin(), dp.end()) << std::endl;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    solve();
    
    return 0;
}
```

3. Given a number, repeatedly find the sum of digits and replace the number. Keep doing this until the number has only a single digit. Print the product of the original number and the single digit.

```python
number = int(input())
temp = number

while temp >= 10:
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
    
    temp = sum

print(number * temp)
```

4. There are `n` number of rooms in a house. You are given a string `s` of length `2n-2` with upper and lower case characters. Lower case characters represent keys and Upper case characters represent rooms. All odd indices (1-based) are keys and even indices are rooms. To unlock a room, you need to have its corresponding key. Count the number of rooms for which you'll have to additionally purchase keys if you start from room 1 and visit all rooms in the order given in the string.

Example:

```
4
aAbBcC

Answer: 0. You can visit all rooms without purchasing any keys.

5
aAcBbCaB

Answer: 1. You need to purchase key `b` for room `B` at index 4 (1-based).
```

```cpp
#include <bits/stdc++.h>

void solve() {
  int n;
  std::string s;
  std::cin >> n >> s;

  std::multiset<char> keys;
  int ans = 0;

  for (int i = 0; i < n - 1; ++i) {
    char key = s[2 * i];
    char door = s[2 * i + 1];
    keys.insert(key);

    auto f = keys.find(std::tolower(door));
    if (f == keys.end())
      ++ans;
    else
      keys.erase(f);
  }

  std::cout << ans << '\n';
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  solve();

  return 0;
}
```

5. You are given a string `s` and integer `k`. You need to encode the string using the following algorithm:
- Traverse s from left to right
- If the character is a vowel, you need to increment k by 2. Otherwise, increment k by 1.
- The value corresponding to the current character is its ASCII value times k

Example:

```
abecd 1

Answer: [291, 392, 606, 693, 800]
0: 97 * 3 = 291
1: 98 * 4 = 392
2: 101 * 5 = 606
3: 99 * 6 = 693
4: 100 * 7 = 800
```

Solution is to simulate the above behaviour.

6. Given `n` numbers, count the unique numbers subject to the following constraints:
- A number is unique if it is the maximum number in the collection and has only one occurrence.
- If maximum number has more than one occurrence, it is not unique and all its occurrences are removed from the collection.
- If maximum number has only one occurrence, it is unique. The number `max` is removed from the occurence and floor(max / 2) is added to the collection if it is greater than 0.

Example:

```
5
1 2 3 4 5

Answer: 3
0: [1, 2, 3, 4, 5], unique = 0 + 1 = 1 (5 is unique)
1: [1, 2, 3, 3, 4], unique = 1 + 1 = 2 (4 is unique)
2: [1, 2, 2, 3, 3], unique = 2 + 0 = 2 (3 is not unique and all occurrences are removed)
3: [1, 2, 2], unique = 2 + 0 = 2 (2 is not unique and all occurrences are removed)
4: [1], unique = 2 + 1 = 3 (1 is unique)
5: [], answer = 3
```

```cpp
#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> v(n);
  for (int i = 0; i < n; ++i)
    std::cin >> v[i];

  std::map<int, int> map;
  for (int i: v)
    ++map[i];
  
  int ans = 0;
  while (!map.empty()) {
    auto [k, v] = *map.rbegin();
    map.erase(k);
    if (k / 2 > 0)
      ++map[k / 2];
    if (v == 1)
      ans += 1;
  }

  std::cout << ans << '\n';
  
  return 0;
}
```

## Round 3 (Ideation)

> 03/10/2023 - 10/10/2023

Yet to happen.

## Round 4 (Prototype)

> 12-10-2023 - 24-10-2023

Yet to happen.

## Round 5 (Finale)

> 03-11-2023 - 05-11-2023

Yet to happen.
