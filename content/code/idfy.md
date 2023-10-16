# [IDfy](https://www.idfy.com/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 6 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE | Internship |
|--------|-----|------------|
| Base   | --  | --         |
| Stocks | --  | --         |
| Bonus  | --  | --         |
| CTC    | 10L | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1

> 16/10/23

[comment]: # (Summary of the sections and experience below this comment.)

### Coding Questions

3 Coding questions and 1 SQL

#### Coding

1. **Preprocess Dates**: Given a list of dates in the format `5-Mar-2023` convert it to `2023-03-05`.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
unordered_map<string, string> months = {
    {"Jan", "01"},
    {"Feb", "02"},
    {"Mar", "03"},
    {"Apr", "04"},
    {"May", "05"},
    {"Jun", "06"},
    {"Jul", "07"},
    {"Aug", "08"},
    {"Sep", "09"},
    {"Oct", "10"},
    {"Nov", "11"},
    {"Dec", "12"},
};


vector<string> preprocessDate(vector<string> dates) {
    vector<string> res;
    for (auto date: dates) {
        int i = 0;
        string day = "";
        string month = "";
        string year = "";
        string t = "";
        while (date[i] != ' ') {
            if (date[i] - '0' < 10 && date[i] - '0' >= 0) {
                t += date[i];
            }
            ++i;
        }
        ++i;
        
        if (t.size() == 1) {
            day += '0';
        }
        day += t;
        t = "";
        
        while (date[i] != ' ') {
            t += date[i];
            ++i;
        }
        ++i;
        
        month = months[t];
        t = "";
        
        while (i < date.size()) {
            t += date[i];
            ++i;
        }
        year = t;
        res.push_back(year + "-" + month + "-" + day);
    }
    
    return res;
}
```

---

2. **Nuts & Bolts**: There are two numbers, a secret number and a guess number, the number of digits in the guess number that are in the correct position of the secret number refer to as nuts.

    Whereas, the number of digits in the guess number that are in the secret number but at the wrong position is refered to as bots.

    Print it as `xAyB` where x is nuts and y is bolts.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
string solve(string secret, string guess) {
    int nuts = 0;
    int bolts = 0;
    int n = secret.size();
    
    unordered_set<int> incorrect;
    unordered_map<char, int> remaining;
    
    for (int i = 0; i < n; ++i) {
        if (secret[i] == guess[i]) {
            ++nuts;
        }
        else {
            ++remaining[secret[i]];
            incorrect.insert(i);
        }
    }
    
    for (int idx: incorrect) {
        if (remaining[guess[idx]] != 0) {
           ++bolts;
           --remaining[guess[idx]];
        }
    }    
    return to_string(nuts) + "A" + to_string(bolts) + "B";
}
```

---

3. **Error Logs**: Given a list of error logs in the format of `[date, time, type, status]`, return only those logs which are of type `ERROR` or `CRITICAL` and return them in the sorted order of date and time. If two logs appear at the same time, give priority to the one that appears first.

[comment]: # (Add any resources or links or code to this question under this comment.)

```cpp
string helper(string date, string time) {
    string year = "";
    string month = "";
    string day = "";
    
    string t = "";
    for (int i = 0; i < date.size(); ++i) {
        if (date[i] == '-') {
            if (day == "") {
                day = t;
            }
            else {
                month = t;
            }
            t.clear();
            continue;
        }
        t += date[i];
    }
    year = t;
    return year + month + day + time;
}

vector<vector<string>> extractErrorLogs(vector<vector<string>> logs) {
    vector<pair<string, int>> l;
    string log_string = "";
    
    for (int i = 0; i < logs.size(); ++i) {
        auto log = logs[i];
        if (log[2] == "ERROR" || log[2] == "CRITICAL") {
            log_string += helper(log[0], log[1]);
            l.push_back({log_string, i});
        }
        log_string.clear();
    }
    
    sort(l.begin(), l.end());
    
    vector<vector<string>> res;
    
    for (auto p: l) {
        res.push_back(logs[p.second]);
    }
    return res;
}
```

---

#### SQL

4. **CPU Usage**: Two tables, servers (int id, varchar(255) cidr) and usage (int id, varchar(255) cpu_usage, varchar(255) network_usage, varchar(255) system_usage) are given.

    Display the server ip's that have a cpu_usage of over a threshold, display the average of all the usages for all the listings for that server ip.

    Threshold: 80%

    Servers
    | id | cidr           |
    |----|----------------|
    | 1  | 192.168.1.0/24 |
    | 2  | 171.xxx.y.z/16 |

    Usage
    | id | cpu_usage | network_usage | system_usage |
    |----|-----------|---------------|--------------|
    | 1  | 1%        | 50%           | 7%           |
    | 2  | 81%       | 5%            | x%           |
    | 3  | 75%       | x%            | y%           |
    | 2  | 23%       | x%            | y%           |
    | 1  | 46%       | x%            | y%           |
    | 2  | 95%       | x%            | y%           |
    | 3  | 72%       | x%            | y%           |
    | 2  | 23%       | x%            | y%           |

    - id 2 has one or more listings with more than 80% cpu_usage so display the avg of all listings of id 2

    Output
    | cidr           | cpu_usage | network_usage | system_usage |
    |----------------|-----------|---------------|--------------|
    | 171.xxx.y.z/16 | 66.34%    | x%            | y%           |

[comment]: # (Add any resources or links or code to this question under this comment.)

---
