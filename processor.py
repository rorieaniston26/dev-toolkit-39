"""Processor module for dev-toolkit-39.
Handles data processing with validation.
"""

def is_valid_input(value):
    if isinstance(value, (int, float)) and value > 0:
        return True
    return False

def validate_and_process(data):
    if not is_valid_input(data):
        raise ValueError("Invalid input: must be positive number")
    # Perform processing
    processed = data * 2 + 1  # some operation
    return processed

def main():
    # Main processing loop
    inputs = [10, 5.5, -2, 0, 20, "text", 15]
    processed_results = []
    for idx, item in enumerate(inputs):
        print(f"Processing item {idx + 1}: {item}")
        try:
            if not isinstance(item, (int, float)):
                raise ValueError("Input must be numeric")
            if item <= 0:
                raise ValueError("Input must be positive")
            result = validate_and_process(item)
            processed_results.append(result)
            print(f"  Result: {result}")
        except ValueError as err:
            print(f"  Error: {err}. Skipping.")
    print("\nAll processed results:", processed_results)

if __name__ == "__main__":
    main()