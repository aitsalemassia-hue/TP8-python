
import csv
from datetime import datetime


class BatchProcessor:

     def __init__(self, fichier_csv):
          self.fichier_csv = fichier_csv
          self.fichier = None
          self.journal = None
          self.reader = None

     def __enter__(self):
          try:
               self.fichier = open(self.fichier_csv, "r", encoding="utf-8")
               self.journal = open("journal.log", "a", encoding="utf-8")
               self.reader = csv.reader(self.fichier)

               self.journal.write("Début du traitement global\n")
               return self

          except (OSError, csv.Error) as e:
               print("Erreur d'ouverture :", e)
               self.__exit__(None, None, None)
               raise

     def traiter(self):
          try:
               for ligne in self.reader:
                    if not ligne:
                         continue

                    operation = ligne[0]
                    date = datetime.now()

                    self.journal.write(
                         f"{date} - Début : {operation}\n"
                    )

                    print("Traitement de :", operation)

                    self.journal.write(
                         f"{datetime.now()} - Fin : {operation}\n"
                    )

          except (OSError, csv.Error) as e:
               print("Erreur de traitement :", e)
               raise

     def __exit__(self, exc_type, exc_value, traceback):
          if self.journal:
               try:
                    self.journal.write("Fin du traitement global\n")
               except OSError:
                    print("Erreur d'écriture dans le journal")
               finally:
                    self.journal.close()

          if self.fichier:
               self.fichier.close()

          if exc_type:
               print("Une exception s'est produite :", exc_value)

          return False



