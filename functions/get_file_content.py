import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        os_abspath_workD = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(os_abspath_workD, file_path))
        validate_target_path = os.path.commonpath([os_abspath_workD, target_path]) == os_abspath_workD
        if validate_target_path:
            if os.path.isfile(target_path) == False:
                return f'Error: File not found or is not a regular file: "{file_path}"'

            with open(target_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1):
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        else:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
        
#Schema: Getting file content        
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the file content for specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Retrieve the file's content",
            ),
        },
    ),
)
    
