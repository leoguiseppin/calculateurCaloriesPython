
# Trouver son nombre de calories

erreur = "Erreur. Veuillez essayer a nouveau."

# 1. Calculer le nombre de calories idéal
# 2. Le mettre à l'essai pendant un certain temps
# 3. L'ajuster si nécessaire en fonction du resultat
poids = float(input("Veuillez entrer votre poids en kg : "))
taille = float(input("Veuillez entrer votre taille en cm : "))
age = float(input("Veuillez entrer votre age : "))
sexe = input("Veuillez entrer votre sexe (M/F) : ")

if sexe != "M" and sexe != "m" and sexe != "F" and "f" :
    print(erreur)
    sexe = input("Veuillez entrer votre sexe (M/F) : ")

# Multiplicateur [M] :
print("1. Peu ou pas d'exercice/sport dans la semaine")
print("2. 1 heure a 3 heures de sport par semaine")
print("3. 4 heures a 6 heures de sport intense par semaine")
print("4. Plus de 6 heures de sport par semaine et un travail physique")
multiplicateur = int(input("A quelle fréquence faites-vous du sport ? (1/2/3/4) : "))

if multiplicateur != 1 and multiplicateur != 2 and multiplicateur != 3 and multiplicateur != 4 :
    print(erreur)
    multiplicateur = int(input("A quelle fréquence faites-vous du sport ? (1/2/3/4) : "))

if multiplicateur == 1 :
    multiplicateurDActivite = 1.15
elif multiplicateur == 2 :
    multiplicateurDActivite = 1.25
elif multiplicateur == 3 :
    multiplicateurDActivite = 1.40
elif multiplicateur == 4 :
    multiplicateurDActivite = 1.55

# Formule de Mifflin St.Jeor
# Hommes = 10*poids(kg) + 6.25*taille(cm) - 5*âge(an) + 5
def maintenanceHomme(p,t,a,multipliDActivite) :
    metabolismeDeBase = 10*p + 6.25*t - 5*a + 5
    # Maintenance = métabolisme_de_base [mifflin st.jeor] * multiplicateur_d'activité [M]
    maintenance = metabolismeDeBase*multipliDActivite
    return int(maintenance)

# Femmes = 10*poids(kg) + 6.25*taille(cm) - 5*âge(an) - 161
def maintenanceFemme(p,t,a,multipliDActivite) :
    metabolismeDeBase = 10*p + 6.25*t - 5*a - 161
    # Maintenance = métabolisme_de_base [mifflin st.jeor] * multiplicateur_d'activité [M]
    maintenance = metabolismeDeBase*multipliDActivite
    return int(maintenance)

if sexe == "M" :
    maintenance = maintenanceHomme(poids,taille,age,multiplicateurDActivite)
    print("Votre maintenance est de ", maintenance, " par jour.")
elif sexe == "F" :
    maintenance = maintenanceFemme(poids,taille,age,multiplicateurDActivite)
    print("Votre maintenance est de ", maintenance, " par jour.")

questionMasse = input("Voulez-vous prendre de la masse (O/N) : ")

if questionMasse != "O" and questionMasse != "o" and questionMasse != "N" and questionMasse != "n" :
    print(erreur)
    questionMasse = input("Voulez-vous prendre de la masse (O/N) : ")

def priseMasseSeche(maintenance) :
    objectif = maintenance*1.15
    return int(objectif)

if questionMasse == "O" or questionMasse == "o" :
    maintenance = priseMasseSeche(maintenance)

print("Vous aurez alors besoin de ", maintenance, " calories par jour.")