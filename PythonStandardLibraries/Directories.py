# File and Directories Manipulation

from pathlib import Path

path = Path(r"c:\College\Git")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("Git-Learn")


for file in path.iterdir():
    print(file)

# paths = [file for file in path.iterdir() if file.is_dir()]
# print(paths)  # Returns Windows path files

txtFiles = [p for p in path.glob("*.txt")]
print(txtFiles)
