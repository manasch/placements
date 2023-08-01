# [Commvault](https://www.commvault.com/)


## Details

### Job Status

01/08/23

Full Time( Employment + Internship Mandatory)

### Criteria

|Study|Cutoff|
|-----|------|
|X|75%|
|XII|75%|
|UG|80%|


### Compensation

||FTE|Internship|
|--|-----|------|
|Base|16,00,000|--|
|Stocks|19000 USD|--|
|Joining Bonus|1,50,000|--|
|Relocation Bonus|75000|--|
|CTC|32.99LPA|50000|

## OA

Two job roles were offered, QA and SDE, QA only had python as an option and SDE had an option between JAVA and CPP, I chose CPP. Had 13 MCQ and 3 Coding

### Questions

1. Reverse alternate m nodes in a linked list.

> A function to reverse a linked list given head and apply this every other m nodes.

```cpp
```

2. Given a BST, and two values p and q, find the largest value in the path from p to q. Both p and q exist.

> Find the lowest common ancestor and traverse right.

```cpp
int solve(Node *head, int p, int q) {
    Node *p1 = head;
    while (true) {
        if (p1->data > p && p1->data > q) {
            p1 = p1->left;
        }
        else if (p1->data < p && p1->data < q) {
            p1 = p1->right;
        }
        else {
            break;
        }
    }

    int maxVal = max(p, q);
    int result = 0;
    while (p1 != maxVal) {
        if (p1->data > maxVal) {
            p1 = p1->left;
        }
        else if (p1->data < maxVal) {
            p1 = p1->right;
        }
        result = max(result, p1->data);
    }
    return result;
}
```

3. A mountain of q meters high exists, with q-1 supports spaced out every 1 meter. Can jump at most r supports at once. Starting from the bottom find the total number of ways to reach the peak.

> Have a DP array and keep updating its values from right to left.

```cpp
int solve(int q, int r) {
    vector<int> dp(q);
    while (int i = q - 1; i >= 0; --i) {
        int count = 0;
        for (int j = 1; j < r; ++j) {
            if (i + j == q) {
                ++count;
            }
            else if (i + j < q) {
                count += dp[i + j];
            }
            else {
                break;
            }
        }
        dp[i] = count;
    }
    return dp[0];
}
```
---
