import json

def save_key(key, filename):
    with open(filename, 'w') as file:
        json.dump({"key": key}, file)

def load_key(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data["key"]
