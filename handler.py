import time
import random
import functools
from typing import Callable, Any

def retry_with_backoff(retries: int = 3, backoff_in_seconds: int = 1):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        raise e
                    
                    sleep = (backoff_in_seconds * 2 ** x +
                             random.uniform(0, 1))
                    time.sleep(sleep)
                    x += 1
        return wrapper
    return decorator

@retry_with_backoff(retries=3, backoff_in_seconds=2)
def fetch_network_data(url: str) -> str:
    """Simulated network request with potential failure."""
    # Example implementation logic
    import urllib.request
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
    try:
        data = fetch_network_data('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Request failed after retries: {e}')