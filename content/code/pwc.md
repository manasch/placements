# [PwC Acceleration Centers](https://www.linkedin.com/company/pwc-acceleration-centers)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff    |
|-------|-----------|
| X     | %         |
| XII   | %         |
| UG    | 60%/6 GPA |

- Cyber Security as Major or Elective

## Round 1: Cyber Recruit Boot Camp

> 08/08/23

There were 4 sections:
1. Computer Fundamental MCQs (16)
2. Cybersecurity MCQs (16)
3. Coding Question - Easy (1)
4. Coding Question - Novice (1)

Coding Questions had a choice of C, Java and Python. Questions were different for everyone.

### Questions

#### Coding Question - Easy

1. Remove duplicates from string

> A function to remove all duplicate alphabets and non-alphabetic characters from a string and sort it in ascending order. The resultant string was supposed to be lower-case.

```python3
def solve(str):
  str = sorted(str.lower())
  res = ""
  for i in str:
    if i.isalpha() and i not in res:
      res += i
  return res 
```

---

#### Coding Question - Novice

1. Special Number

> A function to return "Special number" if any of the digits in the number were perfect squares of 1, 2 or 3, otherwise return "Not a special number"

```python3
def solve(n):
  while n != 0:
    if n % 10 in [1,4,9]:
      return "Special number"
    n //= 10
  return "Not a special number"
```

---
