from contextlib import ExitStack
from datetime import datetime
from gestionnaireConnection import ConnectionManager

# Partie 2 : fichier de logs + connexion
print(" Partie 2 ")
with ExitStack() as stack:
     log = stack.enter_context(open("log.txt", "a"))
     conn = stack.enter_context(ConnectionManager("Serveur X"))
     log.write(f"[{datetime.now()}] Tâche effectuée sur {conn.service_name}\n")
print("log.txt fermé :", log.closed)

# Partie 3 : simulation d'erreur
print("\n Partie 3 ")
try:
     with ExitStack() as stack:
          log = stack.enter_context(open("log.txt", "a"))
          conn = stack.enter_context(ConnectionManager("Base Y"))
          try:
               raise RuntimeError("Erreur de traitement")
          except RuntimeError as e:
               log.write(f"[{datetime.now()}] ERREUR sur {conn.service_name} : {e}\n")
               raise
except RuntimeError as e:
     print("Exception interceptée :", e)
print("log.txt fermé :", log.closed)