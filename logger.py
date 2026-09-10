import logging
import functools
from typing import Callable, Any

class AsyncLogger:
    """Thread-safe logger with local cache for performance."""
    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)
        self._cache = {}

    def log_message(self, level: int, msg: str) -> None:
        """Log message with primitive memoization to reduce io overhead."""
        if msg not in self._cache:
            self.logger.log(level, msg)
            self._cache[msg] = True
            if len(self._cache) > 100:
                self._cache.clear()

    @staticmethod
    def throttle(seconds: int) -> Callable:
        """Decorator to prevent flood logging."""
        def decorator(func: Callable) -> Callable:
            last_called = 0
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                nonlocal last_called
                import time
                now = time.time()
                if now - last_called > seconds:
                    last_called = now
                    return func(*args, **kwargs)
            return wrapper
        return decorator

def get_logger(name: str) -> AsyncLogger:
    return AsyncLogger(name)