# [IBM](https://www.ibm.com/)

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
|Base|--|--|
|Stocks|--|--|
|Bonus|150000|--|
|CTC|1700000LPA|--|

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 10/09/23

[comment]: # (Summary of the sections and experience below this comment.)

There was only one section with 2 coding questions. Everyone got 2 questions from a pool of questions.

### Coding Questions

1. **New Array**: Given a list of integers and a list of intervals, for each interval, inverst the sign of the numbers with the interval, At the end return how the list would like like. (Follow 1-Based indexing).

Ex: L = [1, -4, 5, 3], intervals = [[2, 4], [1, 3]]
First Interval : [1, 4, -5, 3]
Second Interval: [-1, -4, 5, -3]
The array after applying reversal of sign for all intervals should be returned.

[comment]: # (Add any resources or links or code to this question under this comment.)

2. **Circles Relationship**: Given a list of strings such that each string contains the centres and radii of 2 circles, return a list of same length determining whether the circles:
Intersect at two points, Touch, Concentric, Disjoint-Outside, Disjoint-Inside

String would be: "x1 y1 r1 x2 y2 r1" and all the circle would either be centred on the x-axis or y-axis.

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
def euclidian(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def solve(circles):
    for circle in circles:
        x1, y1, r1, x2, y2, r2 = [int(x) for x in circle.strip().split()]

        dist = euclidian(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            print("Concentric")
        if r1 + r2 == dist or max(r1, r2) - min(r1, r2) == dist:
            print("Touching")
        if max(r1, r2) - min(r1, r2) < d < r1 + r2:
            print("Intersecting")
        if r1 + r2 < dist:
            print("Disjoint-Outside")
        else:
            print("Disjoint-Inside")
```

3. **Compare JSON**: Given two json strings, find the difference between the common keys.

[comment]: # (Add any resources or links or code to this question under this comment.)

4. **Nth Factor**: Given a number, return the Nth factor.
Ex: K = 10, factors are: 1, 2, 5, 10, if n = 3, then 5 should be returned

> Find factors till sqrt(K) as the rest would repeat or be the inverse of the factors existing.

[comment]: # (Add any resources or links or code to this question under this comment.)

---
