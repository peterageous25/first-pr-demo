def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def summarise(numbers):
    return {
        "mean": mean(numbers),
        "median": median(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
