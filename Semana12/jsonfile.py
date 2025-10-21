import json

# Example data to write to JSON
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}

# Writing to JSON file
def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Reading from JSON file
def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Example usage
if __name__ == "__main__":
    # Write data to JSON file
    write_json('data.json', data)
    
    # Read data from JSON file
    loaded_data = read_json('data.json')
    print("Loaded data:", loaded_data)