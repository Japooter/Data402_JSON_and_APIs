import json

car_data = {
    "name": "mercedes",
    "engine": "various"

}

print(car_data)
print(type(car_data))

# json.dumps() --> Turn python dict into a string

car_data_json_string = json.dumps(car_data)

print(car_data_json_string)

print(type(car_data_json_string))

# json.dump() --> Converts dict to a string but also puts it in a file.
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)
