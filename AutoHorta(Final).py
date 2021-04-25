import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis do problema
air_temp = ctrl.Antecedent(np.arange(0, 51, 1), 'air_temp')
air_h = ctrl.Antecedent(np.arange(0, 101, 1), 'air_humidity')
s_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_moisture')
balance = ctrl.Antecedent(np.arange(0, 421, 1), 'balance')

pumping = ctrl.Consequent(np.arange(0,11,1), 'pumping')

# Cria manualmente o mapeamento entre valores nítidos e difusos
s_moisture ['dry'] = fuzz.trapmf(s_moisture.universe, [0,0,10,22])
s_moisture ['moderate'] = fuzz.trapmf(s_moisture.universe, [13,22,28,37])
s_moisture ['wet'] = fuzz.trapmf(s_moisture.universe, [28,40,100,100])

air_h ['low'] = fuzz.trapmf(air_h.universe, [0, 0, 70, 85])
air_h ['high'] = fuzz.trapmf(air_h.universe, [75, 90, 100, 100])

air_temp ['cool'] = fuzz.trapmf(air_temp.universe, [0,0,22,34])
air_temp ['hot'] = fuzz.trapmf(air_temp.universe, [22,34,50,50])

balance ['little'] = fuzz.trapmf(balance.universe, [0,0,120,140])
balance ['average'] = fuzz.trapmf(balance.universe, [120,140,280,300])
balance ['much'] = fuzz.trapmf(balance.universe, [280,300,420,420])

pumping ['veryshort'] = fuzz.trapmf(pumping.universe, [0,0,1,3])
pumping ['short'] = fuzz.trapmf(pumping.universe, [1,3,4,6])
pumping ['average'] = fuzz.trapmf(pumping.universe, [4,6,7,9])
pumping ['long'] = fuzz.trapmf(pumping.universe, [7,9,10,10])

s_moisture.view()
air_h.view()
air_temp.view()
balance.view()

pumping.view()

# Cria as regras de decisão difusa
rule1 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['wet'] & balance['much'], pumping['long'])
rule2 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['wet'] & balance['much'], pumping['short'])
rule3 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['wet'] & balance['much'], pumping['short'])
rule4 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['wet'] & balance['much'], pumping['veryshort'])
rule5 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['moderate'] & balance['much'], pumping['long'])
rule6 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['moderate'] & balance['much'], pumping['average'])
rule7 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['moderate'] & balance['much'], pumping['short'])
rule8 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['moderate'] & balance['much'], pumping['short'])
rule9 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['dry'] & balance['much'], pumping['long'])
rule10 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['dry'] & balance['much'], pumping['long'])
rule11 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['dry'] & balance['much'], pumping['average'])
rule12 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['dry'] & balance['much'], pumping['average'])
rule13 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['wet'] & balance['little'], pumping['short'])
rule14 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['wet'] & balance['little'], pumping['short'])
rule15 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['wet'] & balance['little'], pumping['short'])
rule16 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['wet'] & balance['little'], pumping['veryshort'])
rule17 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['moderate'] & balance['little'], pumping['average'])
rule18 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['moderate'] & balance['little'], pumping['short'])
rule19 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['moderate'] & balance['little'], pumping['short'])
rule20 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['moderate'] & balance['little'], pumping['veryshort'])
rule21 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['dry'] & balance['little'], pumping['long'])
rule22 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['dry'] & balance['little'], pumping['average'])
rule23 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['dry'] & balance['little'], pumping['average'])
rule24 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['dry'] & balance['little'], pumping['short'])
rule25 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['wet'] & balance['average'], pumping['average'])
rule26 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['wet'] & balance['average'], pumping['short'])
rule27 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['wet'] & balance['average'], pumping['short'])
rule28 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['wet'] & balance['average'], pumping['veryshort'])
rule29 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['moderate'] & balance['average'], pumping['average'])
rule30 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['moderate'] & balance['average'], pumping['short'])
rule31 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['moderate'] & balance['average'], pumping['short'])
rule32 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['moderate'] & balance['average'], pumping['short'])
rule33 = ctrl.Rule(air_h['low'] & air_temp['hot'] & s_moisture['dry'] & balance['average'], pumping['long'])
rule34 = ctrl.Rule(air_h['high'] & air_temp['hot'] & s_moisture['dry'] & balance['average'], pumping['long'])
rule35 = ctrl.Rule(air_h['low'] & air_temp['cool'] & s_moisture['dry'] & balance['average'], pumping['average'])
rule36 = ctrl.Rule(air_h['high'] & air_temp['cool'] & s_moisture['dry'] & balance['average'], pumping['short'])

#Criando e simulando um controlador nebuloso
sistema_controle = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24,
rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

#Valores para teste
sistema.input['air_temp'] = 40
sistema.input['air_humidity'] = 20
sistema.input['soil_moisture'] = 60
sistema.input['balance'] = 350

#Computando o resultado
sistema.compute()
print(sistema.output['pumping'])
pumping.view(sim = sistema)