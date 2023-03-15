import json

f = open("dados.json")

data = json.load(f)

totalBilling = 0
numberOfDays = 0
higerBilling = float('-inf')
lowerBilling = float('inf')

for day in data:
    billing = day['valor']
    if billing == 0:
        continue
    totalBilling += billing
    numberOfDays += 1
    if billing < lowerBilling:
        lowerBilling = billing
    if billing > higerBilling:
        higerBilling = billing

averageBilling = totalBilling / numberOfDays

aboveAverage = 0
for day in data:
    if day['valor'] > averageBilling:
        aboveAverage += 1

print('Menor faturamento por dia:', lowerBilling)
print('Maior faturamento por dia:', higerBilling)
print('Número de dias com faturamento acima da média:', aboveAverage)

f.close()
