import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    os_abspath_workD = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(os_abspath_workD, file_path))
    validate_target_dir = os.path.commonpath([os_abspath_workD, target_dir]) == os_abspath_workD

    if not validate_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'    
    if not os.path.isfile(target_dir):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not target_dir.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file' 

    try:
        command = ["python", target_dir]  

        if args is not None:
            command.extend(args)
            
        completed_object = subprocess.run(command, 
                            cwd=os_abspath_workD, 
                            stderr=subprocess.PIPE, 
                            stdout=subprocess.PIPE, 
                            text=True,
                            timeout=30)
                            
        #build return string
        resulting_parts = []

        if completed_object.returncode != 0:
            resulting_parts.append(f"Process exited with code {completed_object.returncode}")
        if not completed_object.stdout and not completed_object.stderr:
            resulting_parts.append("No output produced")
        if completed_object.stdout:
            resulting_parts.append(f"STDOUT:{completed_object.stdout}")
        if completed_object.stderr:
            resulting_parts.append(f"STDERR:{completed_object.stderr}")
        return "\n".join(resulting_parts)
    except Exception as e:
        return f"Error: executing Python File: {e}"

#Schema: Run python file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python scripts",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script",
                items=types.Schema(type=types.Type.STRING)
            )
        },
    ),
)
