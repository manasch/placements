# [Hyperface](https://www.hyperface.co/)

## Details

### Job Status

Full Time (Employment + Internship Mandatory)

### Criteria

| Study | Cutoff |
|-------|--------|
| X     | %      |
| XII   | %      |
| UG    | 8 GPA  |

[comment]: # (Any other details go under this. This is a comment)

### Compensation

|        | FTE    | Internship |
|--------|--------|------------|
| Base   | 14 LPA | 30000      |
| Stocks | 3 L    | --         |
| Bonus  | 3 L    | --         |
| CTC    | ~20 L  | --         |

[comment]: # (Details about the rounds go under this comment.)

## Round 1 - Coding Round

> 18/08/23

[comment]: # (Summary of the sections and experience below this comment.)

There was only 1 question and we were given 2 hours.

### Coding Questions

1. **Chef's Dishes**: A chef wants to cook dishes, he gets one new ingredient each day, and this ingredient can be one of 5 types. (Protein, Carb, Fibre, Fat, Seasoning), and each type has an expiry date.
The ingredient would be as follows: Fat1, CarbsRice, ProtienChicken, Fibre1...

    Fat - 1 (If received on Day 1, can be used on Day 1 or Day 2, but expires after Day 2)
    Carbs - 3
    .
    .

    A dish is prepared when it meets the following conditions:
    - It uses exactly M ingredients
    - It uses exactly N categories (Fat, Fibre etc).

    The expected output is as follows:
    - If the chef can cook on a day with the ingredients he has, print out the ingredients used in the order of their arrival separated by ":".
    ex: Fat1:Fibre2:Carbs1.
    - If the chef cannot cook then print "#".
    - If the chef can cook on a day he will mandatorily make the dish.

[comment]: # (Add any resources or links or code to this question under this comment.)

---

## Round 2 - Design Round

- Design an in-memory sophisticated cache that handles the following

    - Eviction Strategy: LRU, LFU.
    - Write Policy: Write-Through, Write-Behind.
    - TTL: Delete data from cache after ttl has expired.
    - Cache Misses: Determine the number of cache misses at any point in time.
    - Configurable cache size

- A two page document was provided with function declarations and details.
- Could pick any language of our choice, usage of internet was allowed but no LLM's

---
