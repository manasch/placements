# [Hiver](https://hiverhq.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | 80%    |
| XII   | 80%    |
| UG    | 8 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE     | Internship |
|--------|---------|------------|
| Base   | 1000000 | 25000      |
| Stocks | --      | --         |
| Bonus  | 100000  | --         |
| CTC    | 1100000 | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 07/10/23

[comment]: # (Summary of the sections and experience below this comment.)

There were only 7 questions, 5 MCQ and 2 Coding, in 1h15m

### Coding Questions

1. **Next Smallest Palindrome**: Given a number as an array, find the next smallest palindrome.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
vector<int> solve(vector<int> num) {
    bool isPalin = false;
    int n = num.size();

    auto helper = [&] () {
        int l = 0;
        int r = n - 1;
        int t, oldr, p;
        while (l < r) {
            oldr = num[r];
            num[r] = num[l];

            if (oldr > num[l]) {
                t = r - 1;
                while (t > 0) {
                    p = num[t];
                    ++p;

                    if (p < 10) {
                        num[t] = p;
                        break;
                    }
                    else {
                        num[t] = 0;
                    }
                    --t;
                }
                --l;
                ++r;
            }
            ++l;
            --r;
        }

        if (l >= r) {
            isPalin = true;
        }
    };

    while (!isPalin) {
        helper();
    }

    return num;
}
```

---

2. **Covid Beds**: There is a line of beds represented by 1's and 0's in a string, 1 means that the bed is occupied and 0 means that the bed is vacant. A partition is defined as such that it has exactly 2 occupied beds (this can also mean that the parition can have vacant beds too).

    A partition is created by placing a temporary walls between any two beds.

    Print the number of ways the walls can be placed such that partitions satisfying the conditions can be made. If no such partitions can be made, print -1.

    Ex:
    ```text
    6
    110011

    Output: 3 - [11|0011, 110|011, 1100|11]

    6
    101101

    Output: 1 - [101|101]

    11
    11001100011

    Output: 12
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

---
