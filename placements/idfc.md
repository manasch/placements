# [IDFC First](https://www.idfcfirstbank.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | 60%    |
| XII   | 60%    |
| UG    | 6 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|          | FTE     | Internship |
|----------|---------|------------|
| Base     | 14L     | --         |
| Variable | 2.1L    | --         |
| Bonus    | 2L      | --         |
| CTC      | 18.1LPA | 40000      |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 17/11/23

[comment]: # (Summary of the sections and experience below this comment.)

There were 3 sections.

1. Aptitude (15) - 20 min
2. Technical (25) - 25 min (Had MS Excel and Stats too for some reason)
3. Coding (2) - 45 min

### Coding Questions

1. **Distribute Cookies**: There are N people sitting in a circle, the people are numbered from 1...N. There's a ball that player 1 holds and has to pass it on to other players. A random number K is selected which determines the distance any player has to pass the ball.

    When the ball returns to player 1, that round is over, and you have to print out the players who did not touch the ball.

    If each player touched the ball before it goes back to 1, then print 0.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
void solve(int n, int k) {
    vector<bool> persons(n + 1, true);
    int person = 1;
    int count = 1;
    persons[person] = false;
    while ((person + k) % n != 1) {
        person = (person + k) % n;
        persons[person] = false;
        ++count;
    }

    if (count == n) {
        cout << "0" << endl;
    }
    else {
        for (int i = 1; i <= n; ++i) {
            if (persons[i]) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
}
```

---

2. **Word Location**: The input is a line of words seperated by space. You have to print the word and its position if the word starts with a vowel; if these words were sorted in ascending order.

    Print 0 if there are no words that start with a vowel.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
bool isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'O' || ch == 'I' || ch == 'O' || ch == 'U'
}

void solve(string words) {
    vector<string> wordss;
    string temp;
    for (char ch: words) {
        if (ch == ' ') {
            wordss.push_back(temp);
            temp = "";
            continue;
        }
        temp += ch;
    }
    wordss.push_back(temp);

    sort(wordss.begin(), wordss.end());

    bool flag = true;
    for (int i = 0; i < n; ++i) {
        string word = wordss[i];
        if (isVowel(word[0])) {
            flag = false;
            cout << word << " " << i + 1 << endl;
        }
    }

    if (flag) {
        cout << "0" << endl;
    }
}
```

---

## Round 2

> 22/11/23

This was a technical round, was asked about OOPS, Strings, C++ (because it was in my resume)

3 coding questions were asked

1. Given an array of numbers, and a value target, use the minimum number of numbers from the array to sum up to the target value.
2. Find out if a number is an armstrong number or not.
3. Find out if two strings are anagrams of each other.

---

## Round 3

> 22/11/23

This was a technical + HR round, it was different for different people.

Was asked about projects in my resume and how oauth2 works, was given 1 coding question.

1. Given an array of characters which can contain duplicates, print the string which is the lexicographically largest and doesn't contain any of the dupes.
> I told the set approach first, and then was asked to implement it without a set. Did it using sorting.

Other basic HR questions.

1. What do I know about IDFC?
2. Why do I want to join IDFC?
3. What have I done in the past 6 months to help in my career growth?
4. How would you handle relocation and situations?

---
