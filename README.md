# Highest Value Longest Common Subsequence (HVLCS)

## Team
- Alejandro Wakszol (UFID: 42739040)
- [Partner Name] (UFID: [Partner UFID])

## Description
Given two strings A and B over a fixed alphabet with character values, this program computes a common subsequence that maximizes the total value and outputs both the maximum value and the subsequence.

## Build / Run
No compilation needed (Python 3).

```bash
python src/hvlcs.py <input_file>
```

### Example
```bash
python src/hvlcs.py data/example.in
```

Expected output:
```
9
cb
```

## Input Format
```
K
x1 v1
x2 v2
...
xK vK
A
B
```
- `K`: number of characters in the alphabet
- Each of the next K lines: a character and its integer value
- `A`: first string
- `B`: second string

## Output Format
- Line 1: the maximum value of a common subsequence
- Line 2: one optimal common subsequence achieving that value

## Example Files
- Input: [`data/example.in`](data/example.in)
- Output: [`data/example.out`](data/example.out)

## Assumptions
- Input files follow the format described above.
- Character values are nonnegative integers.
- Strings contain only characters defined in the alphabet.

## Questions

### Question 1: Empirical Comparison
*TODO*

### Question 2: Recurrence Equation
*TODO*

### Question 3: Big-Oh
*TODO*
