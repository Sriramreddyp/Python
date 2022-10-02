from pathlib import Path

# Absoulute path
path = Path(r"c:\College\Git")
print(path)
# Path() / "E-commerce" / "__init__.py"
# Path.home()
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_name("file.txt")
print(path.absolute())
