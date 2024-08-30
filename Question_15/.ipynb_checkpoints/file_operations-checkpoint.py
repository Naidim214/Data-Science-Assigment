# file_operations.py

def read_file(file_path):
    """
    Reads the entire content of a file.
    
    Args:
    file_path (str): The path to the file to read.
    
    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, data):
    """
    Writes data to a file. Overwrites the file if it already exists.
    
    Args:
    file_path (str): The path to the file to write.
    data (str): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path, data):
    """
    Appends data to the end of a file. Creates the file if it does not exist.
    
    Args:
    file_path (str): The path to the file to append.
    data (str): The data to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(data)
