# [Endor Labs](https://www.endorlabs.com/)

## Details

### Job Status

Internship Only (With possible conversion based on performance)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 8 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE | Internship |
|--------|-----|------------|
| Base   | --  | 100000     |
| Stocks | --  | --         |
| Bonus  | --  | --         |
| CTC    | --  | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 04/11/23

[comment]: # (Summary of the sections and experience below this comment.)

### Coding Questions

1. **Log Files**: A bank has transaction logs in the form of "sender_user_id receiver_user_id amount". Given multiple such logs in an array and a threshold value of transactions, return a list of the user_id's whose total transaction count is greater than the threshold in ascending order.

    Example:
    ```md
    88 99 200
    99 20 100
    20 99 200
    12 12 200

    | ID | Transactions |
    |----|--------------|
    | 88 | 1            |
    | 99 | 3            |
    | 20 | 2            |
    | 12 | 1            |

    > 12 is considered as just 1 transaction as it is a self-transfer
    
    Output:
    ['20', '99']
    ```

[comment]: # (Add any resources or links or code to this question under this comment.)

---

2. **Good Binary Strings**: A binary string is a string consisting of 0's and 1's.

    A good binary string is defined as follows:

    1. The number of 1's is the same as the number of 0's
    2. For every prefix in the string, the number of 1's is not less than the number of 0's

    You are given a good binary string. This string can contain multiple good binary substrings.

    If two substrings are good and are adjacent (no overlap) to each other, they can be swapped. Perform zero or more swaps of such adjacent good substrings on the given binary string to get the lexicographically largest string.

    > They didn't mention binary string here, so I'm assuming it is the lexicographically largest string.

[comment]: # (Add any resources or links or code to this question under this comment.)

---

3. **Coding Friends**: Two friends Erica and Bob like to solve questions, each day they solve one question.

    There are 3 types of questions:

    | Type | Points |
    |------|--------|
    | E    | 1      |
    | M    | 3      |
    | H    | 5      |

    Two lists are given that entail what problems both solve every day.

    Print 'Erica', 'Bob' or 'Tied' depending on who has the higher points at the end of all the problems.

[comment]: # (Add any resources or links or code to this question under this comment.)

---
