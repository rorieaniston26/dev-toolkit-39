import re
from typing import Any, Dict, Optional

# Configuration for input validation constraints
MAX_INPUT_LENGTH = 1024
ALLOWED_PATTERN = re.compile(r'^[a-zA-Z0-9_\-\.]+$')

def validate_payload(data: Dict[str, Any]) -> bool:
    """Validates dictionary keys and string values for safe processing."""
    if not isinstance(data, dict):
        return False

    for key, value in data.items():
        # Ensure keys are strings and not empty
        if not isinstance(key, str) or not key:
            return False
            
        # Validate string length and allowed characters
        if isinstance(value, str):
            if len(value) > MAX_INPUT_LENGTH:
                return False
            if not ALLOWED_PATTERN.match(value):
                return False
                
    return True

def sanitize_input(value: Any) -> Any:
    """Basic sanitization for generic input processing."""
    if isinstance(value, str):
        return value.strip()
    return value

def process_safe_input(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Main gateway for sanitized data injection into logic."""
    if validate_payload(data):
        return {k: sanitize_input(v) for k, v in data.items()}
    return None