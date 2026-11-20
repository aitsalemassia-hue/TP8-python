from pathlib import Path
from contextlib import contextmanager, ExitStack


class TempFileWriter:
    def __init__(self, name="temp.txt"):
        self.filepath = Path(name)

    def __enter__(self):
        self.f = self.filepath.open("w")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        self.filepath.unlink(missing_ok=True)
        return False


@contextmanager
def temp_file(name="temp2.txt"):
    path = Path(name)
    f = path.open("w")
    try:
        yield f
    finally:
        f.close()
        path.unlink(missing_ok=True)


# Partie 1
with TempFileWriter() as f:
    f.write("Contenu temporaire\n")
print("temp.txt existe encore :", Path("temp.txt").exists())  # False

# Partie 2
with temp_file() as f:
    f.write("Autre test\n")
print("temp2.txt existe encore :", Path("temp2.txt").exists())  # False

# Partie 3
paths = ["rapport.txt", "script.txt", "livrable.txt"]
files = []
try:
    with ExitStack() as stack:
        files = [stack.enter_context(open(p, "w")) for p in paths]
        for i, f in enumerate(files):
            f.write("test\n")
            if i == 1:
                raise RuntimeError("Erreur simulée")
except RuntimeError as e:
    print("Exception interceptée :", e)

print([f.closed for f in files])  