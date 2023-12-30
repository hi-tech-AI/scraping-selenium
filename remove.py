import json

with open('output.json') as file:
    data = json.load(file)

unique_elements = set()

# Create a new list to store non-duplicate elements
deduplicated_data = []

for item in data:
    # Convert the item to a tuple based on the desired key(s) for uniqueness
    item_tuple = tuple(item.items())

    # Check if the item is already in the set of unique elements
    if item_tuple not in unique_elements:
        # Add the item tuple to the set of unique elements
        unique_elements.add(item_tuple)

        # Append the item to the new list of non-duplicate elements
        deduplicated_data.append(item)

# Update the original data with the deduplicated data
data = deduplicated_data    

print(len(data))

with open('category9.json', 'w') as file:
    json.dump(data, file)