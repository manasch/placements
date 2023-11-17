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

2. **Word Location**: The input is a line of words seperated by space. You have to print the index and word if these words were sorted by ascending order if the word starts with a vowel.

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
