import matplotlib
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ------------------------- définition de fonction d'appartenance ----------------------

temperarute = ctrl.Antecedent(np.arange(14, 27, 0.1), "temperarute")
temperarute['faible'] = fuzz.trapmf(temperarute.universe, [14, 14, 17, 19])
temperarute['moyenne'] = fuzz.trimf(temperarute.universe, [17, 20, 23])
temperarute['élevée'] = fuzz.trapmf(temperarute.universe, [21, 23, 25.5, 26])

humidite = ctrl.Antecedent(np.arange(52, 101, 0.1), "humidite")
humidite['Sec'] = fuzz.trapmf(humidite.universe, [52, 52, 80, 84])
humidite['Humide'] = fuzz.trapmf(humidite.universe, [68, 84, 99, 100])

vitesse = ctrl.Consequent(np.arange(0, 101, 1), 'vitesse')

vitesse['faible'] = fuzz.trapmf(vitesse.universe, [0, 0, 30, 40])
vitesse['moyenne'] = fuzz.trapmf(vitesse.universe, [30, 45, 60, 70])
vitesse['élevée'] = fuzz.trapmf(vitesse.universe, [60, 75, 99, 100])

# afficher les fonction :
temperarute.view()
humidite.view()
vitesse.view()

# ---------------------------------------- base de régle -------------------------------------

regle_1 = ctrl.Rule(temperarute['faible'] | humidite['Sec'], vitesse['faible'])
regle_2 = ctrl.Rule(temperarute['moyenne'] & humidite['Humide'], vitesse['moyenne'])
regle_3 = ctrl.Rule(temperarute['élevée'], vitesse['élevée'])

# regle_1.view() afficher comme réseau de neurones
# peut ajouter plusieur nombre de regle selon leur condition

# ajouter les regle au simulation controle
vitesse_ctrl = ctrl.ControlSystem([regle_1, regle_2, regle_3])
sumilation = ctrl.ControlSystemSimulation(vitesse_ctrl)

# deux valeur entree
sumilation.input['temperarute'] = 18
sumilation.input['humidite'] = 80
# calculer
sumilation.compute()
print(" La valeur floue de cette base de regle : ", sumilation.output['vitesse'])

# afficher resultat dans fonction
vitesse.view(sim=sumilation)
