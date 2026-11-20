
from pathlib import Path
from gestionnaireFile import TempFileWriter, temp_file
from contextlib import ExitStack


print("        PARTIE 1       ")

with TempFileWriter("exemple.txt") as f:
     f.write("Contenu temporaire\n")
     print("Écriture dans exemple.txt réussie")

print("exemple.txt existe encore :", Path("exemple.txt").exists())


print("\n      PARTIE 2       ")

with temp_file("exemple2.txt") as f:
     f.write("Autre test\n")
     print("Écriture dans exemple2.txt réussie")

print("exemple2.txt existe encore :", Path("exemple2.txt").exists())


print("\n       PARTIE 3           ")

paths = ["rapport.txt", "script.txt", "livrable.txt"]
files = []

try:
     with ExitStack() as stack:

          # Ouvrir les trois fichiers
          files = [
               stack.enter_context(open(p, "w", encoding="utf-8"))
               for p in paths
          ]

          # Écrire dans chaque fichier
          for i, f in enumerate(files):
               f.write("Test d'écriture\n")
               print("Écriture dans", paths[i], "réussie")

               # Simuler une exception
               if i == 1:
                    raise RuntimeError("Erreur simulée")

except RuntimeError as e:
     print("Exception interceptée :", e)


# Vérifier la fermeture des fichiers
print("État des fichiers :", [f.closed for f in files])
