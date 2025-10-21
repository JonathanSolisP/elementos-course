import os

def create_folder(path):
    try:
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)
        print(f"Folder created successfully at: {path}")
    except Exception as e:
        print(f"Error creating folder: {e}")

# Example usage
folder_path = "Semana12/new_folder"
create_folder(folder_path)