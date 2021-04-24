import numpy as np
from numpy import array
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

umid = ctrl.Antecedent(np.arange(0, 101, 1), 'umid')

umid.universe
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
91,  92,  93,  94,  95,  96,  97,  98,  99, 100])

umid
Antecedent: umid

temp = ctrl.Antecedent(np.arange(0, 51, 1), 'temp')
irrig = ctrl.Consequent(np.arange(30,101,30), 'irrig')

umid.automf(number=3, names=['Seco', 'Médio', 'Úmido'])
temp ['Frio'] = fuzz.trimf(temp.universe, [0,0,18])
temp ['Agradável'] = fuzz.trimf(temp.universe, [18,24,50])
temp ['Quente'] = fuzz.trimf(temp.universe, [24,50,50])
umid.view()
temp.view()

irrig ['ligada'] = fuzz.trimf(irrig.universe, [30, 30, 60])
irrig ['manter'] = fuzz.trimf(irrig.universe, [30, 60, 90])
irrig ['desligada'] = fuzz.trimf(irrig.universe, [60, 90, 90])

regra1 = ctrl.Rule(temp['Frio'] & umid['Seco'], irrig['ligada'])
regra2 = ctrl.Rule(temp['Frio'] & umid['Médio'], irrig['manter'])
regra3 = ctrl.Rule(temp['Frio'] & umid['Úmido'], irrig['desligada'])
regra4 = ctrl.Rule(temp['Agradável'] & umid['Seco'], irrig['ligada'])
regra5 = ctrl.Rule(temp['Agradável'] & umid['Médio'], irrig['manter'])
regra6 = ctrl.Rule(temp['Agradável'] & umid['Úmido'], irrig['desligada'])
regra7 = ctrl.Rule(temp['Quente'] & umid['Seco'], irrig['ligada'])
regra8 = ctrl.Rule(temp['Quente'] & umid['Médio'], irrig['ligada'])
regra9 = ctrl.Rule(temp['Quente'] & umid['Úmido'], irrig['desligada'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['temp'] = 50
sistema.input['umid'] = 66
sistema.compute()
print(sistema.output['irrig'])
irrig.view(sim = sistema)