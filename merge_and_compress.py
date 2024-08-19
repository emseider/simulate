import os
import re

def remove_comments_and_docstrings(source):
    """
    Remove comments and docstrings from the source code.
    """
    pattern = re.compile(r"""
        (?P<comments>\#.*?$)        |  # Match comments
        (?P<docstrings>             # Match docstrings (single-line or multi-line)
            (\"\"\".*?\"\"\")       |
            (\'\'\'.*?\'\'\')
        )
    """, re.VERBOSE | re.DOTALL | re.MULTILINE)
    
    return re.sub(pattern, "", source)

def rename_functions(source, prefix):
    """
    Rename all functions in the source code by adding a prefix to avoid name conflicts.
    """
    pattern = re.compile(r"def\s+(\w+)\s*\(")
    
    def replacer(match):
        return f"def {prefix}_{match.group(1)}("
    
    return re.sub(pattern, replacer, source)

def merge_python_files(input_folder, output_file, prefix):
    """
    Merge all Python files in the input_folder into a single file, remove comments,
    and rename functions with the given prefix.
    """
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith('.py') and file != os.path.basename(__file__) and file != output_file:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        source_code = infile.read()
                        source_code = remove_comments_and_docstrings(source_code)
                        source_code = rename_functions(source_code, prefix)
                        outfile.write(f"\n# --- Start of {file} ---\n\n")
                        outfile.write(source_code)
                        outfile.write(f"\n# --- End of {file} ---\n\n")
    print(f"All Python files have been merged into {output_file}")

def create_build_folder(build_folder):
    """
    Create a build folder if it doesn't exist.
    """
    if not os.path.exists(build_folder):
        os.makedirs(build_folder)
        print(f"Build folder '{build_folder}' created.")
    else:
        print(f"Build folder '{build_folder}' already exists.")

if __name__ == "__main__":
    # Define the folder containing the Python files
    input_folder = '.'  # Current directory
    
    # Define the build folder name
    build_folder = 'build'
    
    # Define the output merged file name
    output_file = os.path.join(build_folder, 'build_script.py')
    
    # Define a prefix for renaming functions to avoid conflicts
    prefix = 'merged'
    
    # Create the build folder
    create_build_folder(build_folder)
    
    # Merge all Python files
    merge_python_files(input_folder, output_file, prefix)
