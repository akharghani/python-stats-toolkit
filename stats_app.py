"""Command-line app that asks for numbers and prints a summary using mystats."""

import mystats

def main():
    """Run the interactive Elementary Statistics App.

    This function:
        prompts the user to enter a list of numbers separated by commas,
        then converts the input text into a list of float values,
        and calls mystats.summary() to compute basic statistics, and
        prints the results or an error message if the input is invalid.
    Args:
        None
    Returns:
        None
    """
    print("Welcome to Elementary Statistics App! ")
    print("Enter a list of numbers separated by commas.")
    print("Example: 1, 2, 4.5, 9")

    try:
        input_text = input("Numbers: ")
        parts = input_text.split(",")
        values =[]
        for x in parts:
            stripped = x.strip()
            if stripped == "":
                raise ValueError("Empty value found in the list of numbers!")
            number = float(stripped)
            values.append(number)

        stats = mystats.summary(values)
        print("Summary of your data:")
        print(f"Count : {stats['count']}")
        print(f"Sum   : {stats['sum']}")
        print(f"Mean  : {stats['mean']}")
        print(f"Median: {stats['median']}")
        print(f"Range : {stats['range']}")

    except ValueError as v:
        print("There was a problem with your input or data:")
        print(v)

if __name__ == "__main__":
    main()
