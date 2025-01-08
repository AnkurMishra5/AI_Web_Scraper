# File handling utilities
import os

def save_to_file(data, file_path):
    """Saves data to a specified file."""
    with open(file_path, "w") as file:
        file.write(data)