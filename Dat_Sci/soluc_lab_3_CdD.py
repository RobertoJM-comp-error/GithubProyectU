import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

path = kagglehub.dataset_download("sibamsamanta07/movies-dataset-45k-films-with-budget-and-revenue")
print("Carpeta del dataset:", path)

# Ver qué archivos hay dentro de la carpeta descargada
print(os.listdir(path))

# Una vez sepas el nombre del csv, arma la ruta completa
csv_path = os.path.join(path, "movies_metadata.csv")
df = pd.read_csv(csv_path)

print(df.head(3))

print(df.isna().sum())

subset_df = df.iloc[10000:20000].copy()

bi_subset_df = subset_df["runtime"]

ai_subset_df = bi_subset_df.interpolate(method='linear')

print("Resultado de interpolar:")
print(ai_subset_df)

plt.figure(figsize=(10, 5))
plt.plot(bi_subset_df.index, bi_subset_df.values, label='Original', marker='o')
plt.plot(ai_subset_df.index, ai_subset_df.values, label='Interpolado', marker='x')
plt.title('Interpolación de duración de películas')
plt.xlabel('Índice de película')
plt.ylabel('Duración (minutos)')
plt.legend()
plt.grid()
plt.show()
plt.savefig('interpolation_comparison.png', dpi=300, bbox_inches='tight')

class Resistencia:
    def __init__(self, nombre: str, valor_ohmios: float, tolerancia_pct: float):
        self.nombre = nombre
        self.valor_nominal = valor_ohmios
        self.tolerancia = tolerancia_pct

    def obtener_descripcion(self):
        return print(f"Resistencia {self.nombre}: {self.valor_nominal} ohmios ±{self.tolerancia}%")

resist_R1 = Resistencia("R1", 220, 5) #220omh
resist_R1.obtener_descripcion()

class Bateria:
    def __init__(self, voltaje_nom: float, capacidad_mAh: float):
        self.voltaje = voltaje_nom
        self.capacidad = capacidad_mAh

    def ener_total(self):
        return self.voltaje * self.capacidad / 1000   # Energía en vatios-hora (Wh)
Bateria (12, 2000)  # 12V, 2000mAh
print(f"Energía total de la batería: {Bateria.ener_total(Bateria(12, 2000))} Wh")

class Multimetro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    @staticmethod
    def mediciones_v(min, max, cant):
        # Genera una lista de mediciones de voltaje aleatorias dentro de un rango especificado.
        mediciones_v = np.random.uniform(min, max, cant)
        if np.any(mediciones_v < 0):
            print("Advertencia: Se han generado mediciones de voltaje negativas, revisar modo de medición.")
        return print(mediciones_v)
        #mediciones_v_pos = mediciones_v[mediciones_v > 0]  # Filtra solo los valores positivos
        #return mediciones_v_pos

mediciones_v = Multimetro.mediciones_v(-50, 50, 10)  # Genera 10 mediciones de voltaje entre -50 y 50v

class PanelSolar:
    def __init__(self, superficie_m2: float, eficiencia_pct: float):
        self.superficie = superficie_m2
        self.eficiencia = eficiencia_pct
        self.historial_potencias = []  # Lista para almacenar las potencias registradas

    def generar_potencia(self, irradiancia_w_m2: float):
        return self.superficie * irradiancia_w_m2 * (self.eficiencia / 100)  # Potencia en vatios (W)

    def registar_potencia(self, potencia: float):
        self.historial_potencias.append(potencia)  # Agrega la potencia al historial
        return self.historial_potencias

print (f"Potencia generada por el panel solar: {PanelSolar(1.5, 20).generar_potencia(1000)} W")  # Superficie de 1.5 m² y eficiencia del 20% con irradiancia de 1000 W/m²
print (f"Historial de potencias: {PanelSolar(1.5, 20).registar_potencia(PanelSolar(1.5, 20).generar_potencia(1000))}")


 
