class CopyFile:
    def __init__(self, file, copy_file):
        self.file = file
        self.copy_file = copy_file

    def __enter__(self):
        with open(self.file, 'r') as f:
            self.result = f.read()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.copy_file, 'w') as f:
            f.write(self.result)


with CopyFile('file.txt', 'copy_file.txt') as read:
    print(read)
