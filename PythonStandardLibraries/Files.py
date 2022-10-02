from pathlib import Path
from time import ctime
import shutil

Source = Path(r"c:\College\Git\amy\Tokyo\file1.txt")
target = Path() / "file1.txt"

target.write_text(Source.read_text())
shutil.copy(Source, target)

# path.exists()
# path.rename("init.txt")
# path.unlink()

# print(ctime(path.stat().st_ctime))

# path.read_bytes()
# path.read_text()
# path.write_text("Eyoo nigga")
# path.read_text()
