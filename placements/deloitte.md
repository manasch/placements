# [Deloitte](https://www.deloitte.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff  |
|-------|---------|
| X     | %       |
| XII   | %       |
| UG    | 6.5 GPA |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE    | Internship |
|--------|--------|------------|
| Base   | --     | --         |
| Stocks | --     | --         |
| Bonus  | --     | --         |
| CTC    | 760000 | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 03/09/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 4 sections:
1. English Comprehension
2. Aptitude
3. Technical
4. Coding (2)

### Coding Questions

1. **Matching Last Character**: Given a list of words and a character to match, print the sorted position (1-index) of the word with the other words if the last letter of the word matches with the character to match.

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
def solve(inputStr, searchCh):
	words = inputStr.split()
	words.sort()
	for i in range(len(words)):
		if words[i][-1] == searchCh:
			print(words[i], i + 1)
```

---

2. **Largest Digit in a Number**: Given a number, return the largest digit in the number.

[comment]: # (Add any resources or links or code to this question under this comment.)

---
