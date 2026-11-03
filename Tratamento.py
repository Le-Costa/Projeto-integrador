import requests
import json
import pandas as pd
#importação do JSON
url = "http://10.12.22.92:8080/maquinas"

r = requests.get(url)
data = r.json()

print(json.dumps(data, indent=4, ensure_ascii=False))
    
# tratamento 
pd.DataFrame(data)

    
# Acessar os registros
dt = data["dados"]
# Converter para DataFrame
df = pd.DataFrame(dt)
#Exibir máquinas únicas
time = df["timestamp"].unique()


# Separar data e hora usando o T como divisor
df[["data", "hora"]] = df["timestamp"].str.split("T", expand=True)

#print(df[["data", "hora"]])
#remoção dos milisegundos
df["hora"] = df["hora"].str[:-5]
df["data"] = pd.to_datetime(df["data"]).dt.strftime("%d/%m/%Y")

print(df)
#FALTA FAZER UM TRATAMENTO PARA CASO A API NAO CONSIGA ACESSAR
#DEFINIR QTD DE VEZES PARA RODAR, CASO NÃO RODE PARAR. 
