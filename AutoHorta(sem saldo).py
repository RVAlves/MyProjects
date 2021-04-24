import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis do problema
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temp')
u_ar = ctrl.Antecedent(np.arange(0, 101, 1), 'u_ar')
u_solo = ctrl.Antecedent(np.arange(0, 1025, 1), 'u_solo')

irrig = ctrl.Consequent(np.arange(30,101,30), 'irrig')

# Cria manualmente o mapeamento entre valores nítidos e difusos
temp ['frio'] = fuzz.trimf(temp.universe, [0,0,20])
temp ['agradavel'] = fuzz.trapmf(temp.universe, [10,21,22,35])
temp ['quente'] = fuzz.trimf(temp.universe, [22,40,40])

u_ar ['seco'] = fuzz.trapmf(u_ar.universe, [0, 0, 35, 60])
u_ar ['ideal'] = fuzz.trapmf(u_ar.universe, [35, 60, 65, 80])
u_ar ['umido'] = fuzz.trimf(u_ar.universe, [65, 100, 100])

u_solo ['seco'] = fuzz.gaussmf(u_solo.universe, 0, 256)
u_solo ['medio'] = fuzz.gaussmf(u_solo.universe, 512, 256)
u_solo ['umido'] = fuzz.gaussmf(u_solo.universe, 1024, 256)

irrig ['ligar'] = fuzz.trimf(irrig.universe, [30, 30, 60])
irrig ['manter'] = fuzz.trimf(irrig.universe, [30, 60, 90])
irrig ['desligar'] = fuzz.trimf(irrig.universe, [60, 90, 90])

temp.view()
u_ar.view()
u_solo.view()

irrig.view()

# Cria as regras de decisão difusa

# Para temperatura (frio)
rule1 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['seco'], irrig['ligar'])
rule2 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['medio'], irrig['ligar'])
rule3 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['umido'], irrig['desligar']) # Verificar


rule4 = ctrl.Rule(temp['frio'] & u_ar['ideal'] & u_solo['seco'], irrig['ligar'])
rule5 = ctrl.Rule(temp['frio'] & u_ar['ideal'] & u_solo['medio'], irrig['ligar'])
rule6 = ctrl.Rule(temp['frio'] & u_ar['ideal'] & u_solo['umido'], irrig['desligar'])


rule7 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['seco'], irrig['ligar'])
rule8 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['medio'], irrig['ligar'])
rule9 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['umido'], irrig['desligar'])

# Para temperatura (agradavel)
rule10 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['seco'], irrig['ligar'])
rule11 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['medio'], irrig['ligar'])
rule12 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['umido'], irrig['desligar'])


rule13 = ctrl.Rule(temp['agradavel'] & u_ar['ideal'] & u_solo['seco'], irrig['ligar'])
rule14 = ctrl.Rule(temp['agradavel'] & u_ar['ideal'] & u_solo['medio'], irrig['ligar'])
rule15 = ctrl.Rule(temp['agradavel'] & u_ar['ideal'] & u_solo['umido'], irrig['desligar'])


rule16 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['seco'], irrig['ligar'])
rule17 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['medio'], irrig['ligar'])
rule18 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['umido'], irrig['desligar'])

# Para temperatura (quente)
rule19 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['seco'], irrig['ligar'])
rule20 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['medio'], irrig['ligar'])
rule21 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['umido'], irrig['ligar'])


rule22 = ctrl.Rule(temp['quente'] & u_ar['ideal'] & u_solo['seco'], irrig['ligar'])
rule23 = ctrl.Rule(temp['quente'] & u_ar['ideal'] & u_solo['medio'], irrig['ligar'])
rule24 = ctrl.Rule(temp['quente'] & u_ar['ideal'] & u_solo['umido'], irrig['desligar'])


rule25 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['seco'], irrig['ligar'])
rule26 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['medio'], irrig['ligar'])
rule27 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['umido'], irrig['desligar'])


# Criando e simulando um controlador nebuloso
sistema_controle = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24,
rule25, rule26, rule27])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

# Valores para teste
sistema.input['temp'] = 33 # Quente
sistema.input['u_solo'] = 600 # Medio
sistema.input['u_ar'] = 58 # Mais ideal que seco 

# Computando o resultado
sistema.compute()
print(sistema.output['irrig'])
irrig.view(sim = sistema)
