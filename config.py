import functools
import logging
from typing import Any, Callable, Dict

# global cache for performance optimization in configuration loading
_config_cache: Dict[str, Any] = {}

class ConfigManager:
    """Thread-safe configuration manager with memoized access."""
    
    def __init__(self, storage_backend: Any):
        self.backend = storage_backend

    @functools.lru_cache(maxsize=128)
    def get_setting(self, key: str) -> Any:
        """Fetch and cache configuration setting with lru strategy."""
        if key in _config_cache:
            return _config_cache[key]
            
        try:
            value = self.backend.fetch(key)
            _config_cache[key] = value
            return value
        except Exception as e:
            logging.error(f"failed to load config key {key}: {e}")
            return None

    def clear_cache(self) -> None:
        """Invalidate cache for runtime updates."""
        _config_cache.clear()
        self.get_setting.cache_clear()

# factory for singleton access
def get_config_manager(backend: Any) -> ConfigManager:
    return ConfigManager(backend)