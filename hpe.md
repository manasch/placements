# [HPE](https://www.hpe.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

|Study|Cutoff|
|-----|------|
|X|80%|
|XII|80%|
|UG|7 GPA|

[comment]: # (Any other details go under this. This is a comment)

### Compensation

||FTE|Internship|
|--|-----|------|
|Base|--|--|
|Stocks|--|--|
|Bonus|--|--|
|CTC|1750000|40000|

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 06/09/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 4 sections:
1. Aptitude (15) - 20 min
2. Technical (33) - 40 min
3. Coding(2) - 30 min (language 1)
4. Coding(2) - 30 min (language 2)

The options for languages was - cpp, c, python, java

### Coding Questions

#### CPP Coding Nuggets

1. **Palindrome Number**: Given a number, a palindrome can be construced by add the reverse of the number to itself: 12 + 21 = 33. But this is not the case for all numbers for ex: 57.
Find the first palindrome that occurs when performing these operations for the given number.

> Edge case would be when the given number itself is a palindrome.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int reverse(int num) {
    int n = num;
    int res = 0;
    while (n > 0) {
        res = res * 10 + n % 10;
        n = n / 10;
    }
    if (res == num) {
        return 0;
    }
    return res;
}

int palindrome(int N) {
    int num = N;
    int t = reverse(num);
    if (t == 0) {
        num += num;
        t = reverse(num);
    }
    while (t != 0) {
        num += t;
        t = reverse(num);
    }
    return num;
}

int main() {
    int N;
    cin >> n;
    cout << palindrome(N) << endl;
    return 0;
}
```

---

2. **Number of cars**: A car requires 4 wheels (w), 2 chairs (c) and 1 body (b). Given w, c, b, find out the number of cars that can be manufactured.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
int main() {
    int w, c, b;
    cin >> w >> c >> b;
    int count = 0;
    while (w >= 4 && c >= 2 && b >= 1) {
        ++count;
        w -= 4;
        --b;
        c -= 2;
    }
    cout << count << endl;
    return 0;
}
```

---

#### Python Coding Nuggets

3. **Absolute Volume Difference**: Given length, breadth and height of two cubes, find the absolue volume difference between the two.

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
int difference(l1, b1, h1, l2, b2, h2):
    return abs(l1 * b1 * h1 - l2 * b2 * h2)
```

---

4. **New Array**: Given an array, modify it such that the value at the kth position is the sum of the values of it's next two neighbors.

[comment]: # (Add any resources or links or code to this question under this comment.)

```py
int newArray(arr, n):
    lastArr = arr.copy()
    for i in range(n):
        arr[i] = lastArr[(i + 1) % n] + lastArr[(i + 2) % n]
```

---
