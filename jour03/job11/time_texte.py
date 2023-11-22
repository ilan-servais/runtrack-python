# Modifier la fonction time_to_text pour accepter un argument
def time_to_text(minutes):
    try:
        minutes = int(minutes)
        if minutes >= 0:
            heures = minutes // 60
            minutes_restantes = minutes % 60

            if heures == 0 and minutes_restantes == 0:
                print("0 minute")
            elif heures == 0:
                print(f"{minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
            elif minutes_restantes == 0:
                print(f"{heures} heure{'s' if heures > 1 else ''}")
            else:
                print(f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
        else:
            print("Veuillez entrer un nombre entier positif.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Appeler la fonction depuis le terminal avec un argument
import sys

# Récupérer l'argument fourni depuis le terminal
if len(sys.argv) > 1:
    argument = sys.argv[1]
    # Appeler la fonction avec l'argument fourni
    time_to_text(argument)
else:
    print("Veuillez fournir un argument (nombre de minutes) depuis le terminal.")