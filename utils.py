import json

def load_files(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        file_data = json.load(f)
    return file_data

