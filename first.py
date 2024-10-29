import os

# Define the directory structure
structure = {
    "HausaMediaLab": {
        "hausa_media_lib": {
            "__init__.py": "",
            "video_processing.py": "",
            "audio_processing.py": "",
            "file_conversion.py": "",
            "subtitles.py": "",
            "utils.py": "",
        },
        "tests": {
            "__init__.py": "",
            "test_video_processing.py": "",
            "test_audio_processing.py": "",
            "test_file_conversion.py": "",
            "test_subtitles.py": "",
            "test_utils.py": "",
        },
        "README.md": "# HausaMediaLab Library\n\nA Python library for video and audio processing with Hausa translation support.",
        "setup.py": '''from setuptools import setup, find_packages

setup(
    name="HausaMediaLab",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "moviepy",
        "pydub",
        "speech_recognition",
    ],
)
''',
        ".gitignore": "*.pyc\n__pycache__/",
    }
}

# Function to create directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create subdirectories
        else:
            with open(path, 'w') as f:
                f.write(content)  # Create the file and write content

# Create the project structure
base_path = os.getcwd()
create_structure(base_path, structure)

# Function to print directory tree structure
def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

# Print the resulting directory structure
print_tree(os.path.join(base_path, "HausaMediaLab"))
