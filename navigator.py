import os

def __init__(self, root_path):
    self.current_path = os.path.abspath(root_path)
    self.history = []

def list_dir(self):
    try:
        return os.listdir(self.current_path)
    except PermissionError:
        return ["[Acess Denied]"]

