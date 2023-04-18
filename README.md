# JSX-String-Extractor

JSX-String-Extractor is a Python script designed to extract string literals from files in a specified folder, with a focus on supporting JSX components commonly found in React projects. The extracted string literals are saved in a JSON file, making it easy to manage and localize text content.

## About

This script is tailored for extracting string literals from JavaScript, TypeScript, and Python files, but it is especially optimized for handling JSX components in React projects. The script walks through a given folder, processes each file, and stores the extracted string literals in a JSON file with a structured format.

## Installation

1. Make sure you have Python 3.6 or higher installed on your system. You can check your Python version by running `python --version` or `python3 --version` in your terminal or command prompt.

2. Clone this repository to your local machine

3. Navigate to the project folder:

   ```bash
   cd jsx-string-extractor
   ```

4. Run the script with the following command:

   ```bash
   python extract_string_literals.py
   ```

Alternatively, if your default Python version is 2.x, you may need to run the script with Python 3 explicitly:

```bash
python3 extract_string_literals.py
```

5. The script will prompt you to enter the folder path where your files are located. After processing the files, it will generate a JSON file named `string_literals json` with the extracted string literals.
