import json
def jsonValidate(JsonFile):
    try:
        json.loads(JsonFile)
    except ValueError as err:
        return False
    return True
print(jsonValidate())
