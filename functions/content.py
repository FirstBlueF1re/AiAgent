import os
import sys
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        os_abspath_workD = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(os_abspath_workD, file_path))
        validate_target_dir = os.path.commonpath([os_abspath_workD, target_dir]) == os_abspath_workD

        if validate_target_dir == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir, "r") as open_file:
            file_content = open_file.read(MAX_CHARS)    
            if open_file.read(1):
                file_content += f'\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content

    except Exception as e:
        return f'Error: {e}'
