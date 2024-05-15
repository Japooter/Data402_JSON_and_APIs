import json

# json.load() --> Takes a file and converts it into a dictionary

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car)


# json.loads() --> Takes a string, not a file, and converts it into a dictionary.

path_to_json = "example.json"
with open(path_to_json) as json2file:
    json_data = json.loads(json2file.read())

print(json_data)
print(type(json_data))