import json


def serialize_and_save_to_file(data, filename):
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise TypeError("deserialized data must be a dictionary")
    return data
