from gestionnaire_Contexte import BatchProcessor
try:
     with BatchProcessor("exercice3\\test.csv") as batch:
          batch.traiter()

except OSError as e:
     print("Erreur :", e)