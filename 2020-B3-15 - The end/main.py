from io import FileIO
from os import remove
from pathlib import Path


class TempFile(FileIO):
    def __del__(self):
        remove(Path(self.name))


with TempFile("test.txt", "w+") as f:
    f.write("Hello World".encode())
    f.seek(0)
    print(f.read().decode())