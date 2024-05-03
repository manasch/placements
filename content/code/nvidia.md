# [NVIDIA](https://www.nvidia.com/)

## Details

### Job Status

6 Month Internship

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 8 GPA  |

[comment]: # (Any other details go under this. This is a comment)


[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 20/09/23

[comment]: # (Summary of the sections and experience below this comment.)

3 Sections, 60 min and not timed by section.

1. Analytical (15)
2. Technical (12)
3. Coding (2)

### Coding Questions

1. **[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)**

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int lastStoneWeight(vector<int>& stones) {
    priority_queue<int, vector<int>> q(stones.begin(), stones.end());
    int s, t;
    while (q.size() > 1) {
        s = q.top();
        q.pop();
        t = q.top();
        q.pop();

        if ((s - t) != 0) {
            q.push(s - t);
        }
    }

    if (q.size() > 0) {
        return q.top();
    }
    return 0;
}
```

---

2. **Regex Match**: Given a binary representation of a number in string, give the regex pattern to determine if it is a power of 2.

> This was weird, CPP12 language selection had the parsing code already and we just had to mention the regex pattern, whereas CPP14 and CPP20 language selection, we had to take the input and perform the parsing. Nonetheless, parsing can be done with the help of a flag.

[comment]: # (Add any resources or links or code to this question under this comment.)

```
Power of 2 will always have one 1 and 0's on both sides.
0*10*
```

---
