import os

def write_file(working_directory, file_path, content):
    try:
        os_abspath_workD = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(os_abspath_workD, file_path))
        validate_target_dir = os.path.commonpath([os_abspath_workD, target_dir]) == os_abspath_workD

        if not validate_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #create the parent directory so you don't try to make a directory based off the file's name.
        parent_directory = os.path.dirname(target_dir)
        os.makedirs(parent_directory, exist_ok=True)

        with open(target_dir, "w") as open_file:
            open_file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
