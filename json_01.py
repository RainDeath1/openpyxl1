import json

data = {
    "president": {
        "name": "Barak",
        "age": 42
    }
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

with open("data.json", "r", encoding="utf-8") as file:
    new_data = json.load(file)

print(new_data)
