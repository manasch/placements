# [Deutsche](http://www.db.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

|Study|Cutoff|
|-----|------|
|UG|7GPA/70%|

[comment]: # (Any other details go under this. This is a comment)

### Compensation

||FTE|Internship|
|--|-----|------|
|Base|--|--|
|Stocks|--|--|
|Bonus|--|--|
|CTC|19.63 LPA|--|

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 11/08/23

[comment]: # (Summary of the sections and experience below this comment.)

There was only one coding section with 3 questions

### Coding Questions

1. **Minimum length of positive sum subarray**: Given an array with both negative and positive integers, for each index, find the minimum length subarray such that the sum of all elements in that subarray is positive.

> Bruteforce approach passed all the test cases, but otherwise could be solved using sliding window.

[comment]: # (Add any resources or links or code to this question under this comment.)

---

2. **Infinite Multiples**: Given an array of positive integers, and a value `k`, find the k'th largest number among the multiples of each and every element in the given array.

> Create a min-heap and maintain its size to be k and add k multiples for each element in the array, this way the minimum element in a min-heap of size k would be the k'th largest element.

[comment]: # (Add any resources or links or code to this question under this comment.)

---

3. **Maze Runner**: Given a 2-D matrix, each cell takes one of three values.

    '.' - Indicates an open path\
    '#' - Indicates a door (Obstacle)\
    '\*' indicates a wall (Obstacle).

    The person will start at the top-left cell and has to find the shortest path to the bottom-right cell. They can wear two types of glasses, one which allows them to pass through the door and the other to pass through the wall, only one glass can be worn at once, for both the glasses, find the shortest path to reach the destination. If it can't be reached return -1.

> Perform BFS for both cases, could probably be optimized more with DP, not sure.

[comment]: # (Add any resources or links or code to this question under this comment.) 

---
