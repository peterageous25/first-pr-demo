# first-pr-demo

A small Python utility for calculating basic stats on a list of numbers.

## Usage

```python
from stats import summarise

data = [4, 8, 15, 16, 23, 42]
print(summarise(data))
```

## Functions

- `mean(numbers)` — returns the arithmetic mean
- `median(numbers)` — returns the median value
- `summarise(numbers)` — returns a dict with mean, median, min, and max
