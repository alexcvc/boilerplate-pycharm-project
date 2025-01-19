import os


def list_files(directory):
    """List all files in a given directory."""
    if not os.path.exists(directory):
        raise FileNotFoundError(f"{directory} does not exist")
    return os.listdir(directory)


def create_file(file_path, content=""):
    """Create a file with optional content."""
    with open(file_path, 'w') as file:
        file.write(content)

