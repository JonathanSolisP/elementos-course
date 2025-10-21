import pickle

# Create a sample list
my_list = [1, 2, 3, 4, 5, "hello", [10, 20, 30]]

# Save the list to a file using pickle
with open('list_data.jon', 'wb') as file:
    pickle.dump(my_list, file)

print("List has been saved to list_data.pkl")

# Load the list from the file
with open('list_data.jon', 'rb') as file:
    loaded_list = pickle.load(file)

print("List has been loaded from list_data.jon")
for data in loaded_list:
    print(data)