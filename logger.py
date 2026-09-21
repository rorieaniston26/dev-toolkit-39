import logging
import functools
import time

# global cache for logger instances to reduce overhead
_loggers = {}

def get_logger(name: str) -> logging.Logger:
    if name not in _loggers:
        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        _loggers[name] = logger
    return _loggers[name]

def timed_execution(func):
    """decorator for measuring execution time to identify bottlenecks"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger = get_logger('performance')
        logger.debug(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

class PerformanceLogger:
    def __init__(self, name: str):
        self.logger = get_logger(name)

    def log_latency(self, operation: str, duration: float):
        if duration > 0.5:  # threshold for warning on slow operations
            self.logger.warning(f'slow operation detected: {operation} took {duration:.2f}s')
        else:
            self.logger.debug(f'{operation} completed in {duration:.4f}s')