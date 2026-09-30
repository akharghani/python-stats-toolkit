# Python Stats Toolkit

A small beginner project from Introduction to Python course I took in Fall 2025. It was the final project for that course.

It's a basic statistics module (`mystats.py`) plus a command-line app (`stats_app.py`) that asks for a list of numbers and prints a summary. I wrote the calculations with plain loops on purpose, including a simple bubble sort for the median, instead of using Python's built-in `statistics` module or `sorted()`, to practise the fundamentals.

## What it calculates

- Count
- Sum
- Mean
- Median
- Range (max minus min)

Empty lists and invalid input (like letters or a missing number between commas) are caught and show a friendly error message instead of crashing.

## How to run

Requires Python 3. No extra packages.

```
python stats_app.py
```

Example:

```
Numbers: 1, 2, 4.5, 9
Summary of your data:
Count : 4
Sum   : 16.5
Mean  : 4.125
Median: 3.25
Range : 8.0
```

You can also import the functions yourself:

```python
import mystats
mystats.summary([1, 2, 4.5, 9])
```

## Files

- `mystats.py`: the statistics functions
- `stats_app.py`: the interactive program

## Pseudocode

This is the plan I wrote before coding it.

<details>
<summary>Show pseudocode</summary>

```text
BEGIN

Create 2 new python files:
- mystats.py
- stats_app.py

In mystats.py:

Define count_values function with a place to hold the values (numbers):
- if numbers is empty:
    raise an error "numbers list can't be empty"
- go through each item in the list
- keep a counter of how many items in the list
- return counter

Define sum_values function with a place to hold the values (numbers):
- if numbers is empty:
    raise an error "numbers list can't be empty"
- set total to 0
- go through each value in numbers list:
    add the value to the total
- return total

Define mean function with a place to hold the values (numbers):
- if numbers is empty:
    raise an error "numbers list can't be empty"
- get total from the sum_values(numbers) function
- get count from the count_values(numbers) function
- calculate mean_value by dividing the total by count
- return mean_value

Define median function with a place to hold the values (numbers):
- if numbers is empty:
    raise an error "numbers list can't be empty"
- make a sorted copy of numbers as sorted_numbers
- get count by calling count_values(sorted_numbers)
- find the middle number out of the list of numbers and store as middle_index
- if count is odd:
    return the item at middle_index in sorted_numbers
otherwise if count is even:
    left_value is the item at the middle_index - 1 in sorted_numbers
    right_value is the item at the middle_index in sorted_numbers
    return (left_value + right_value) divided by 2

Define data_range function with a place to hold the values (numbers):
- if numbers is empty:
    raise an error "numbers list can't be empty"
- set current_min to the first value of numbers
- set current_max to the first value of numbers
- go through each value in numbers:
    if value is less than current_min:
        update current_min to value
    if value is greater than current_max:
        update current_max to value
- calculate range_value as current_max - current_min
- return range_value

Define summary function with a place to hold the values (numbers):
- get count by calling count_values(numbers)
- get total by calling sum_values(numbers)
- get mean_value by calling mean(numbers)
- get median_value by calling median(numbers)
- get range_value by calling data_range(numbers)
- create a new dictionary called stats
- set stats["count"] to count
- set stats["sum"] to total
- set stats["mean"] to mean_value
- set stats["median"] to median_value
- set stats["range"] to range_value
- return stats

In stats_app.py:

- import mystats
- print a welcome message
- print instructions for the user to follow
- use input to ask the user for numbers separated by commas
- store the string as input_text
- split input_text on commas and store as parts
- create an empty list as values
- start a try block:
    for each text piece in parts:
        strip them from spaces and store as stripped
        if the stripped text is empty:
            raise a value error
        if not then convert the stripped string to a float and store as number
        add the float number to the values list

    call mystats.summary(values) and store as stats

    print a heading for the summary
    print the count value from stats
    print the sum value from stats
    print the mean value from stats
    print the median value from stats
    print the range value from stats

- catch value error as v:
    print a friendly error message about the input
    print the actual error message v

- final check to make sure this file is the main program being executed

END
```

</details>
