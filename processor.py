import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    '''Processes numeric datasets while handling potential data anomalies and edge cases.'''

    def __init__(self, ignore_errors: bool = True):
        self.ignore_errors = ignore_errors

    def calculate_averages(self, datasets: List[Dict[str, Any]]) -> Dict[str, float]:
        '''
        Calculates averages for given datasets.
        Handles edge cases like missing keys, empty lists, non-numeric values, and division by zero.
        '''
        results = {}
        if not isinstance(datasets, list):
            if self.ignore_errors:
                return results
            raise TypeError('Input datasets must be a list of dictionaries')

        for idx, item in enumerate(datasets):
            if not isinstance(item, dict):
                if self.ignore_errors:
                    continue
                raise TypeError(f'Item at index {idx} is not a dictionary')

            name = item.get('name', f'dataset_{idx}')
            values = item.get('values')

            if values is None or not isinstance(values, list):
                if not self.ignore_errors:
                    raise ValueError(f'Dataset {name} is missing a valid values list')
                continue

            # Filter valid numbers to avoid TypeError
            valid_numbers = []
            for val in values:
                if isinstance(val, (int, float)) and not isinstance(val, bool):
                    valid_numbers.append(val)
                elif not self.ignore_errors:
                    raise TypeError(f'Invalid non-numeric value {val} in dataset {name}')

            # Handle division by zero (empty values or no valid numbers)
            if not valid_numbers:
                if self.ignore_errors:
                    results[name] = 0.0
                    continue
                raise ValueError(f'Dataset {name} contains no valid numeric elements for average calculation')

            results[name] = sum(valid_numbers) / len(valid_numbers)

        return results