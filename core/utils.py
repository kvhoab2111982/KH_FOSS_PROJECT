import os

def check_file_exists(file_path):
    """
    Checks if a file exists at the given file path.

    Parameters:
        file_path (str): Path to the file.

    Returns:
        bool: True if file exists, False otherwise.
    """
    return os.path.exists(file_path)
