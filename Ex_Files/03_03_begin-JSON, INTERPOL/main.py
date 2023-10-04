import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)        # Convert dictionary to json
back_to_dict = json.loads(einstein_json)    # Convert json to a dictionary
#print(einstein_json)
#pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

pprint(laureates)


with open("laureates.json", "w") as f:  # w = open in write mode
    json.dump(laureates, f, indent=2)   # create new json file.
