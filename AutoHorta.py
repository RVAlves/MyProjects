import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis do problema
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temp')

u_ar = ctrl.Antecedent(np.arange(0, 101, 1), 'u_ar')

u_solo = ctrl.Antecedent(np.arange(0, 1025, 1), 'u_solo')

saldo = ctrl.Antecedent(np.arange(0, 101, 1), 'saldo')

irrig = ctrl.Consequent(np.arange(30,101,30), 'irrig')

# Cria automaticamente o mapeamento entre valores nítidos e difusos
# usando uma função de pertinência (triângulo)
temp ['frio'] = fuzz.trimf(temp.universe, [0,0,20])
temp ['agradavel'] = fuzz.trapmf(temp.universe, [10,21,22,35])
temp ['quente'] = fuzz.trimf(temp.universe, [22,40,40])

u_ar ['seco'] = fuzz.trapmf(u_ar.universe, [0, 0, 40, 60])
u_ar ['medio'] = fuzz.trapmf(u_ar.universe, [35, 60, 65, 80])
u_ar ['umido'] = fuzz.trimf(u_ar.universe, [65, 100, 100])

u_solo ['seco'] = fuzz.gaussmf(u_solo.universe, 0, 256)
u_solo ['medio'] = fuzz.gaussmf(u_solo.universe, 512, 256)
u_solo ['umido'] = fuzz.gaussmf(u_solo.universe, 1024, 256)

saldo ['pouco'] = fuzz.trimf(saldo.universe, [0,0,20])
saldo ['muito'] = fuzz.trimf(saldo.universe, [0,100,100])

irrig ['ligar'] = fuzz.trimf(irrig.universe, [30, 30, 60])
irrig ['manter'] = fuzz.trimf(irrig.universe, [30, 60, 90])
irrig ['desligar'] = fuzz.trimf(irrig.universe, [60, 90, 90])

# Cria as regras de decisão difusa

# Para temperatura (frio)
rule1 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule2 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule3 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['medio'] & saldo['pouco'], irrig['desligar']) 
rule4 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule5 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule6 = ctrl.Rule(temp['frio'] & u_ar['seco'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])


rule7 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule8 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule9 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule10 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule11 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule12 = ctrl.Rule(temp['frio'] & u_ar['medio'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])


rule13 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule14 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule15 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule16 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule17 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule18 = ctrl.Rule(temp['frio'] & u_ar['umido'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])

# Para temperatura (agradavel)
rule19 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule20 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule21 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule22 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule23 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule24 = ctrl.Rule(temp['agradavel'] & u_ar['seco'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])


rule25 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule26 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule27 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule28 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule29 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule30 = ctrl.Rule(temp['agradavel'] & u_ar['medio'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])


rule31 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule32 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule33 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule34 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule35 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule36 = ctrl.Rule(temp['agradavel'] & u_ar['umido'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])

# Para temperatura (quente)
rule37 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule38 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule39 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule40 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule41 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule42 = ctrl.Rule(temp['quente'] & u_ar['seco'] & u_solo['umido'] & saldo['muito'], irrig['ligar'])


rule43 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule44 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule45 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule46 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule47 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule48 = ctrl.Rule(temp['quente'] & u_ar['medio'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])


rule49 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['seco'] & saldo['pouco'], irrig['desligar'])
rule50 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['seco'] & saldo['muito'], irrig['ligar'])

rule51 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['medio'] & saldo['pouco'], irrig['desligar'])
rule52 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['medio'] & saldo['muito'], irrig['ligar'])

rule53 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['umido'] & saldo['pouco'], irrig['desligar'])
rule54 = ctrl.Rule(temp['quente'] & u_ar['umido'] & u_solo['umido'] & saldo['muito'], irrig['desligar'])

#Criando e simulando um controlador nebuloso
sistema_controle = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24,
rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38,
rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52,
rule53, rule54])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

#Valores para teste
sistema.input['temp'] = 50
sistema.input['u_solo'] = 100
sistema.input['u_ar'] = 20
sistema.input['saldo'] = 20

#Computando o resultado
sistema.compute()
print(sistema.output['irrig'])