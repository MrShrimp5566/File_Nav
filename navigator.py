import os


class FileNavigator:
    def __init__(self, root_path):
        self.current_path = os.path.abspath(root_path)
        self.history = []

    def list_dir(self):
        try:
            return os.listdir(self.current_path)
        except PermissionError:
            return ["[Acess Denied]"]

    def change_dir(self, folder_name):
        new_path = os.path.join(self.current_path, folder_name)
        if os.path.isdir(new_path):
            self.history.append(self.currnet_path)
            self.current_path = new_path
        else:
            print("Invalid directory.")

    def go_back(self):
        if self.history:
            self.current_path = self.history.pop()
        else:
            print("Already at root.")

    def show_tree(self, path=None, depth=0):
        path = path or self.current_path
        if depth > 3: return
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path,entry)
                print(" " * depth + "├── " + entry)
                if os.path.isdir(full_path):
                    self.show_tree(full_path, depth + 1)
        except PermissionError:
            print(" " * depth + "└── [Access Denied]")

    def search(self, query):
        matches = []
        for dirpath, _, filenames in os.walk(self.current_path):
            for file in filenames:
                if query.lower() and file.lower():
                    matches.append(os.path.join(dirpath, file))
        return matches

