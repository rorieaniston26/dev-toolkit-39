import sys

def validate_input(data):
    """Ensures input is a non-empty string under 1024 chars."""
    if not isinstance(data, str):
        return False
    if not (0 < len(data) <= 1024):
        return False
    return True

def run_processing_loop():
    """Main processing loop with input sanitization."""
    print("Starting dev-toolkit-39 processing loop. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input(">> ").strip()
            
            if user_input.lower() == 'exit':
                print("Shutting down.")
                break
            
            if not validate_input(user_input):
                print("Error: invalid input received. Please provide a short string.")
                continue
                
            # Processing logic
            result = user_input.upper()
            print(f"Processed output: {result}")
            
        except (EOFError, KeyboardInterrupt):
            print("\nSession terminated.")
            break
        except Exception as e:
            print(f"Unexpected system error: {e}")

if __name__ == "__main__":
    run_processing_loop()