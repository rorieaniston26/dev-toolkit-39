import re

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_payload(data: dict) -> bool:
    """Ensures payload contains required fields and correct formats."""
    required_fields = {'id', 'payload', 'timestamp'}
    
    if not isinstance(data, dict):
        raise ValidationError("Invalid payload format: dictionary expected")
    
    if not required_fields.issubset(data.keys()):
        missing = required_fields - data.keys()
        raise ValidationError(f"Missing required fields: {missing}")
        
    if not isinstance(data.get('id'), int):
        raise ValidationError("Field 'id' must be an integer")
        
    # Validate alphanumeric string format
    if not re.match(r'^[a-zA-Z0-9]+$', str(data.get('payload'))):
        raise ValidationError("Field 'payload' contains invalid characters")
        
    return True

def sanitize_input(data: str) -> str:
    """Strips whitespace and dangerous characters from raw input."""
    if not data:
        return ""
    return str(data).strip()