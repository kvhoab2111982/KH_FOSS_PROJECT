# Contributors Guide for HausaMediaLab

Welcome to the HausaMediaLab Project! Thank you for considering contributing to this project, which aims to develop a powerful, user-friendly Python library for media processing and Hausa language translation. This document provides guidelines to help you contribute effectively and maintain a high standard of code quality.

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Contribution Workflow](#contribution-workflow)
6. [Development Guidelines](#development-guidelines)
7. [Creating Tests](#creating-tests)
8. [Running Pylint for Code Quality](#running-pylint-for-code-quality)
9. [Submitting Your Contribution](#submitting-your-contribution)
10. [Reporting Issues](#reporting-issues)
11. [Style Guide](#style-guide)
12. [Credits and Acknowledgments](#credits-and-acknowledgments)

---

## 1. Code of Conduct

We follow the Contributor Covenant [Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating in this project, you agree to treat others with respect and professionalism. Any form of harassment or discrimination is strictly prohibited. Please review the Code of Conduct to understand our community standards.

## 2. How to Contribute

You can contribute in various ways:
- Submitting bug reports and feature requests
- Improving documentation
- Reviewing or testing code
- Developing new features or enhancing existing ones

Please check the **Issues** and **Project Board** for specific tasks that need attention. Feel free to reach out on the **Discussions** page for any questions or ideas.

## 3. Project Structure

Understanding the project structure will help you navigate the codebase efficiently.

```plaintext
HausaMediaLab/
├── hausa_media_lib/               # Main library folder with core modules
│   ├── __init__.py                # Package initialization
│   ├── video_processing.py        # Functions for video processing
│   ├── audio_processing.py        # Functions for audio manipulation
│   ├── file_conversion.py         # File format conversion functions
│   ├── subtitles.py               # Subtitle generation and handling functions
│   └── utils.py                   # Utility functions used across modules
├── tests/                         # Folder for test cases for each module
│   ├── __init__.py
│   ├── test_video_processing.py
│   ├── test_audio_processing.py
│   ├── test_file_conversion.py
│   ├── test_subtitles.py
│   └── test_utils.py
├── README.md                      # Project overview and setup instructions
├── CONTRIBUTORS.md                # Guidelines for contributors (this document)
├── setup.py                       # Packaging and installation configuration
└── .gitignore                     # Git ignore file for excluding unnecessary files
```

## 4. Getting Started

1. **Fork the Repository**: Click the fork button at the top of this page to make a copy of the repo in your GitHub account.
2. **Clone Your Fork**: Clone your forked repository to your local machine using:
   ```bash
   git clone https://github.com/your-username/HausaMediaLab.git
   ```
3. **Set Up a Virtual Environment** (recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 5. Contribution Workflow

To maintain code quality and avoid conflicts, please follow these steps:

1. **Sync Your Fork**: Always ensure your fork is up-to-date with the main repository.
2. **Create a New Branch**: Use descriptive names for your branches, such as `add-feature-X` or `fix-bug-Y`.
   ```bash
   git checkout -b add-feature-X
   ```
3. **Make Your Changes**: Write code and tests as required.
4. **Write Tests**: If adding a new feature, include tests in the `tests` folder.
5. **Commit Changes**: Write meaningful commit messages. Follow this format:
   ```
   [MODULE] Brief description of the change
   ```
6. **Push and Submit a Pull Request**:
   ```bash
   git push origin add-feature-X
   ```

After pushing, navigate to the **Pull Requests** tab on GitHub and submit a new pull request.

## 6. Development Guidelines

- **Write Clean Code**: Follow Python best practices and keep code modular.
- **Document Functions**: Include docstrings to explain each function’s purpose, parameters, and return values.
- **Optimize for Efficiency**: Optimize code for speed and memory where possible, especially in media processing functions.

## 7. Creating Tests

Creating reliable tests is essential to maintaining a stable codebase. This project uses the `unittest` library for testing. Tests should be added for each feature, new functionality, or bug fix, and placed within the `tests/` directory. Below are guidelines to help you create effective tests.

### Writing a Test

1. **Organize by Module**: Add tests in files named after the module they’re testing. For example, tests for `video_processing.py` should be added to `test_video_processing.py`.

2. **Create Test Classes**: Define test classes for each group of related tests. Each test class should inherit from `unittest.TestCase`.

3. **Write Test Functions**: Each function in your module should have a corresponding test function prefixed with `test_` in the test file. For example, if you have a function `extract_audio()` in `audio_processing.py`, add a test function called `test_extract_audio()` in `test_audio_processing.py`.

4. **Setup and Teardown**: Use `setUp` and `tearDown` methods in your test classes to handle any necessary setup and cleanup tasks, such as creating or deleting test files.

5. **Check Edge Cases**: Test for common cases, edge cases, invalid inputs, and unexpected scenarios to ensure robust code.

6. **Assert Statements**: Use assertions to verify expected outcomes. Common assertions include:
   - `self.assertEqual()` to check if values are equal.
   - `self.assertTrue()` and `self.assertFalse()` to check for Boolean values.
   - `self.assertRaises()` to check if the right exceptions are raised.

### Example Test

Below is an example of a test case for the `extract_audio()` function in `audio_processing.py`:

```python
import unittest
from hausa_media_lib.audio_processing import extract_audio

class TestAudioProcessing(unittest.TestCase):
    def setUp(self):
        # Setup code for creating a sample test video file, if needed.
        self.sample_video_path = 'sample.mp4'
        self.expected_audio_path = 'sample_audio.wav'

    def test_extract_audio(self):
        # Test if extract_audio produces the correct output.
        output = extract_audio(self.sample_video_path)
        self.assertEqual(output, self.expected_audio_path)
        self.assertTrue(os.path.exists(output))  # Check if output file was created.

    def tearDown(self):
        # Cleanup any files or resources created during the test.
        if os.path.exists(self.expected_audio_path):
            os.remove(self.expected_audio_path)

if __name__ == "__main__":
    unittest.main()
```

### Running Tests

To run all tests in the `tests/` directory, use the following command:

```bash
python -m unittest discover tests
```

This command will automatically find and run all test files prefixed with `test_`. For specific modules, you can specify the path to the test file, for example:

```bash
python -m unittest tests/test_audio_processing.py
```

## 8. Running Pylint for Code Quality

To maintain code consistency and quality, we use `pylint`. **Make sure all `pylint` checks pass** before submitting a pull request.

### How to Run Pylint
1. **Install Pylint** (if not already installed):
   ```bash
   pip install pylint
   ```
2. **Run Pylint on Specific Modules**:
   ```bash
   pylint hausa_media_lib/video_processing.py
   pylint hausa_media_lib/audio_processing.py
   ```
3. **Fix Warnings and Errors**: Address any issues reported by `pylint`. Aim to keep the code’s pylint score above 8.5 for each file.

### Common Pylint Warnings to Fix
- **Naming conventions** (e.g., function names in `snake_case`).
- **Unused imports and variables**.
- **Line length** (try to keep lines under 79 characters).
  
Ensuring `pylint` checks are clean will help keep code standardized and readable.

## 9. Submitting Your Contribution

Once you’re satisfied with your code and have run tests locally:

1. **Check for Merge Conflicts**: Ensure your branch can merge into the `main` branch without conflicts.
2. **Submit a Pull Request** (PR): Explain your changes, referencing any relevant issue numbers.

A maintainer will review your PR, suggest any improvements, and, once approved, merge it into the main branch.

## 10. Reporting Issues

If you find any bugs or issues with the HausaMediaLab library, please follow these steps to report them effectively:

1. **Open a New Issue**: Navigate to the **Issues** tab in the repository and click on the **New Issue** button.
  
2. **Provide a Clear Title**: Write a concise title that summarizes the issue (e.g., "Audio extraction fails for .mp4 files").

3. **Describe the Problem**: In the issue description, provide as much detail as possible, including:
   - A brief description of the problem.
   - Steps to reproduce the issue:
     1. Describe what you did leading up to the issue.
     2. Specify any specific input values used.
   - Expected behavior vs. actual behavior.
   - Screenshots or error messages, if applicable.
  
4. **Environment Details**: Include information about your development environment, such as:
   - Operating System (e.g., Windows, macOS, Linux)
   - Python version (e.g., Python 3.8.10)
   - Any dependencies used (list versions if possible).

5. **Labeling**: If you have a label that applies (e.g., bug, enhancement), add it before submitting the issue.

By providing detailed information, you’ll help the maintainers and contributors understand the problem better and resolve it faster.

## 11. Style Guide

To maintain a consistent code style throughout the HausaMediaLab project, please adhere to the following guidelines:

1. **PEP 8 Compliance**: Follow the [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/) for Python code formatting, including:
   - Indentation: Use 4 spaces per indentation level.
   - Line Length: Limit lines to a maximum of 79 characters.
   - Blank Lines: Use blank lines to separate functions and classes, and larger blocks of code.
  
2. **Naming Conventions**: 
   - Use `snake_case` for functions and variables (e.g., `extract_audio`).
   - Use `CamelCase` for class names (e.g., `AudioProcessor`).
   - Use all uppercase letters with underscores for constants (e.g., `MAX_LENGTH`).

3. **Documentation**: Ensure all functions and classes have docstrings explaining their purpose, parameters, and return values, following the [Google Style Guide for Python](https://google.github.io/styleguide/pyguide.html).

4. **Commenting**: Write clear comments explaining complex or non-obvious sections of the code. Avoid redundant comments that simply repeat what the code does.

5. **Version Control**: When making changes, keep your commit messages concise and relevant. Follow the format: `[MODULE] Brief description of the change`.

6. **Code Reviews**: Be open to feedback on your code during pull requests. Use the review process to learn and improve your coding practices.

## 12. Credits and Acknowledgments

We would like to express our gratitude to everyone who has contributed to the HausaMediaLab project. Your efforts in improving the library and enhancing its functionality are invaluable. 

### Special Thanks
- **Project Maintainers**: For their continuous support and guidance.
- **Contributors**: Every person who has opened issues, submitted pull requests, or provided feedback has helped shape this project.
- **Community Support**: Our community members who have shared ideas and resources, fostering collaboration and innovation.

Let’s continue to work together to make HausaMediaLab an exceptional library for media processing and Hausa language translation!. 🚀
