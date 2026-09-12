import re
from typing import Any, Optional

def validate_payload(data: dict) -> bool:
    """Validate schema and structure of incoming processing data."""
    required_fields = ['id', 'payload', 'timestamp']
    
    if not isinstance(data, dict):
        return False
        
    # Verify all mandatory keys exist
    if not all(field in data for field in required_fields):
        return False
        
    # Sanitize identifier format
    if not isinstance(data['id'], str) or not re.match(r'^[A-Z0-9-]{8,36}$', data['id']):
        return False
        
    return True

def sanitize_input(value: Any) -> Optional[str]:
    """Clean string inputs to prevent injection or malformed data."""
    if not isinstance(value, str):
        return None
        
    # Strip whitespace and control characters
    clean_value = value.strip()
    clean_value = re.sub(r'[\x00-\x1f\x7f]', '', clean_value)
    
    return clean_value if len(clean_value) > 0 else None

def check_processing_constraints(data: dict) -> bool:
    """Check business logic constraints before proceeding."""
    timestamp = data.get('timestamp')
    if not isinstance(timestamp, (int, float)):
        return False
        
    # Ensure data is not older than 24 hours
    import time
    if time.time() - timestamp > 86400:
        return False
        
    return True