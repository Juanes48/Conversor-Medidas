import pandas as pd

# Dataframe es la información básica con el nombre de las piezas y centímetros para poder armar el excel

data = {
    "Piezas" : ["Patas", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros" : [40,110,90,77,130]
}

df = pd.DataFrame(data)

df.to_excel("muebles_medidas.xlsx", index = False)