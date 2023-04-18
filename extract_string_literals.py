import os
import re
import json


def camel_case(word):
    return ''.join(w.capitalize() for w in word.split())


def extract_string_literals(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    regex = re.compile(r'(["\'])(?:(?=(\\?))\2.)*?\1', re.DOTALL)
    string_literals = regex.findall(data)
    string_literals = [s[0] + s[1].strip() + s[0] for s in string_literals]

    jsx_regex = re.compile(r'<[^>]*>[^<>]*</[^>]*>', re.DOTALL)
    jsx_literals = jsx_regex.findall(data)

    for literal in jsx_literals:
        open_tag_end = literal.find('>') + 1
        close_tag_start = literal.rfind('<')
        if open_tag_end < close_tag_start:
            words = literal[open_tag_end:close_tag_start].strip()
            if words:
                string_literals.append(words)

    return string_literals


def process_files_in_folder(folder_path):
    result = {}

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if not file_name.endswith(('.ts', '.tsx', '.js', '.jsx', '.py')):
                continue

            file_path = os.path.join(root, file_name)
            string_literals = extract_string_literals(file_path)

            if not string_literals:
                continue

            formatted_literals = {}
            for string_literal in string_literals:
                first_word = string_literal.split()[0]
                formatted_literals[camel_case(first_word)] = string_literal

            result[file_name] = formatted_literals

    return result


def main():
    folder_path = input("Enter the folder path: ")
    output_file = "string_literals.json"

    results = process_files_in_folder(folder_path)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print(f"String literals extracted and saved to {output_file}")


if __name__ == "__main__":
    main()
