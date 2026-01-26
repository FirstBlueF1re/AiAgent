import os

def get_files_info(working_directory, directory="."):
    try:
        if not directory:
            return f'Error: "{directory}" is not a directory'
        os_abspath_workD = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(os_abspath_workD, directory))
        validate_target_dir = os.path.commonpath([os_abspath_workD, target_dir]) == os_abspath_workD
        if validate_target_dir:
            if os.path.isdir(target_dir) == False:
                return f'Error: "{directory}" is not a directory'

            item_property = []
            for item in os.listdir(target_dir):
                full_path = os.path.join(target_dir, item)
                file_size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                item_property.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
            return "\n".join(item_property)

        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: {e}'
        
