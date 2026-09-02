"""Exceptions for input validation in main processing loop."""
class InputValidationError(Exception):
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value
class MissingFieldError(InputValidationError):
    def __init__(self, field):
        super().__init__(f"Missing required field: {field}", field=field)
class InvalidTypeError(InputValidationError):
    def __init__(self, field, expected_type, actual_type):
        message = f"Field '{field}' expected {expected_type.__name__}, got {actual_type.__name__}"
        super().__init__(message, field=field, value=actual_type)
        self.expected_type = expected_type
class OutOfRangeError(InputValidationError):
    def __init__(self, field, value, min_val, max_val):
        message = f"Field '{field}' value {value} out of range [{min_val}, {max_val}]"
        super().__init__(message, field=field, value=value)
        self.min_val = min_val
        self.max_val = max_val
def validate_string(field, value, min_length=1, max_length=100):
    if not isinstance(value, str):
        raise InvalidTypeError(field, str, type(value))
    length = len(value)
    if length < min_length or length > max_length:
        raise OutOfRangeError(field, length, min_length, max_length)
    return value
def validate_integer(field, value, min_val=0, max_val=1000):
    if not isinstance(value, int):
        raise InvalidTypeError(field, int, type(value))
    if value < min_val or value > max_val:
        raise OutOfRangeError(field, value, min_val, max_val)
    return value
def validate_dict_input(data, required_fields):
    if not isinstance(data, dict):
        raise InvalidTypeError("data", dict, type(data))
    for field, (typ, minv, maxv) in required_fields.items():
        if field not in data:
            raise MissingFieldError(field)
        val = data[field]
        if typ == str:
            validate_string(field, val, minv, maxv)
        elif typ == int:
            validate_integer(field, val, minv, maxv)
    return data
def process_data_batch(batch):
    """Main processing loop implementing input validation."""
    results = []
    for item in batch:
        try:
            validated = validate_dict_input(item, {"name": (str, 1, 50), "age": (int, 0, 120), "score": (int, 0, 100)})
            processed = {"name": validated["name"].upper(), "age": validated["age"], "score": validated["score"] * 1.1}
            results.append(processed)
        except InputValidationError as e:
            print(f"Skipped invalid item: {e}")
    return results