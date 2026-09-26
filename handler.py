import time
import random
from typing import Callable, Any, Optional

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Any:
    """
    Executes a network-related function with exponential backoff.
    """
    attempt = 0
    current_delay = delay
    
    while attempt < retries:
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            attempt += 1
            if attempt >= retries:
                print(f"Final attempt failed: {e}")
                raise e
            
            sleep_time = current_delay + random.uniform(0, 0.1)
            time.sleep(sleep_time)
            current_delay *= backoff
            
    return None

# Example usage demonstration
def network_request():
    # Simulate a flakey network operation
    if random.random() < 0.7:
        raise ConnectionError("Server unreachable")
    return "Success"

if __name__ == "__main__":
    result = execute_with_retry(network_request)
    print(f"Result: {result}")