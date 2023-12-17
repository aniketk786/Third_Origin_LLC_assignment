import json
from jsonschema import validate, ValidationError

class JsonValidator:


    def __init__(self):
        self.schema = None

    def load_schema(self, schema_file: str) -> None:

        with open(schema_file, 'r') as f:
            self.schema = json.load(f)

    def validate_schema(self, json_file: str, integrity_rules_file: str) -> bool:
        if not self.schema:
            raise ValueError("Schema not loaded. Use load_schema() first.")

        # Load JSON data
        with open(json_file, 'r') as f:
            data = json.load(f)

        try:
            validate(instance=data, schema=self.schema)
        except ValidationError as e:
            print(f"Validation Error: {e}")
            return False

        # Applying additional integrity rules
        return self._apply_integrity_rules(data, integrity_rules_file)

    def _apply_integrity_rules(self, data: dict, integrity_rules_file: str) -> bool:

        with open(integrity_rules_file, 'r') as f:
            integrity_rules = json.load(f)


        return True

# Example usage:
validator = JsonValidator()
#provide location to check the file is in .json format or not

validator.load_schema('C:/Users/ANIKET/Downloads/new_example.JSON')

is_valid = validator.validate_schema('C:/Users/ANIKET/Downloads/new_example.JSON', 'C:/Users/ANIKET/Downloads/new_rules.json')

if is_valid:
    print("The JSON file is valid according to the schema and rules.")
else:
    print("Validation failed. There are errors in the JSON file.")

