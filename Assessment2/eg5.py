import json

# Load JSON data from file
with open('ex5.json', 'r') as file:
    example = json.load(file)

# Find and update the specific item in the JSON data
for item in example:
    if item["name"] == "Old Fashioned" and item["type"] == "donut":
        item["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

# Write the updated JSON data back to the file
with open('ex5.json', 'w') as file:
    json.dump(example, file, indent=2)
