"""Basic statistics functions written with plain loops (no statistics library)."""

def count_values(numbers):
    """Return how many values are in the list.
    Args:
        numbers: A list of numeric values.
    Raises:
        ValueError: If the list is empty.
    Returns:
        int: The number of items in the list.
    """
    if numbers == []:
        raise ValueError("numbers list must not be empty.")
    count = 0
    for x in numbers:
        count += 1
    return count

def sum_values(numbers):
    """Return the sum of all values in the list.
    Args:
        numbers: A list of numeric values.
    Raises:
        ValueError: If the list is empty.
    Returns:
        float: The sum of all values in the list.
    """
    if numbers == []:
        raise ValueError("numbers list must not be empty.")
    total = 0
    for value in numbers:
        total = total + value
    return total

def mean(numbers):
    """Return the arithmetic mean (average) of the values.
    The mean is calculated as the sum of the values divided by
    the number of values.
    Args:
        numbers: A list of numeric values.
    Raises:
        ValueError: If the list is empty.
    Returns:
        float: The mean of the values.
    """
    total = sum_values(numbers)
    count = count_values(numbers)
    mean_value = total / count
    return mean_value

def median(numbers):
    """Return the median (middle value) of the list.
    For an odd number of values, the median is the single middle value
    when the list is sorted. For an even number of values, the median
    is the average of the two middle values.
    Args:
        numbers: A list of numeric values.
    Raises:
        ValueError: If the list is empty.
    Returns:
        float: The median of the values.
    """
    if numbers == []:
        raise ValueError("numbers list must not be empty.")
    sorted_numbers = numbers[:]
    count = count_values(sorted_numbers)
    for x in range(count - 1):
        for y in range(0, count - 1 - x):
            if sorted_numbers[y] > sorted_numbers[y + 1]:
                sorted_numbers[y], sorted_numbers[y + 1] = (sorted_numbers[y + 1]
                , sorted_numbers[y])
    middle_index = count // 2
    if count % 2 == 1:
        return sorted_numbers[middle_index]
    else:
        left_value = sorted_numbers[middle_index - 1]
        right_value = sorted_numbers[middle_index]
        return (left_value + right_value) / 2

def data_range(numbers):
    """Return the range of the data (maximum minus minimum).
    Args:
        numbers: A list of numeric values.
    Raises:
        ValueError: If the list is empty.
    Returns:
        float: The range of the data, calculated as max(numbers) - min(numbers).
    """
    if numbers == []:
        raise ValueError("numbers list must not be empty.")
    current_min = numbers[0]
    current_max = numbers[0]
    for x in numbers:
        if x < current_min:
            current_min = x
        if x > current_max:
            current_max = x
    return current_max - current_min

def summary(numbers):
    """Return a dictionary containing basic summary statistics.
    The dictionary contains:
        count: number of values
        sum: sum of all values
        mean: average of all values
        median: median value
        range: maximum minus minimum
    Args:
        numbers: A list of numeric values.
    Returns:
        dict: A dictionary with keys "count", "sum",
            "mean", "median", and "range".
    """
    count = count_values(numbers)
    total = sum_values(numbers)
    mean_value = mean(numbers)
    median_value = median(numbers)
    range_value = data_range(numbers)
    stats = {
        "count" : count,
        "sum" : total,
        "mean" : mean_value,
        "median" : median_value,
        "range" : range_value,
    }
    return stats
