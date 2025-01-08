# Unit tests for utility functions
from src.utils.file_utils import save_to_file

def test_save_to_file(tmp_path):
    file_path = tmp_path / "test.txt"
    data = "Hello, World!"
    save_to_file(data, file_path)

    with open(file_path, "r") as file:
        content = file.read()

    assert content == data