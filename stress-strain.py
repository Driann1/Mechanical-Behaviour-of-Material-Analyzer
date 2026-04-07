import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# === 1. Baca file CSV ===

pilih_material = input("Material apa yang ingin di pilih \n")

file_path_analisis = f"analysis_result/{pilih_material}"
file_path_analisis2 = f"{file_path_analisis}/{pilih_material}.txt"
file_path_curve = f"{file_path_analisis}/{pilih_material}.png"
file_path_data = f"stress_strain_data/{pilih_material}.csv"


Path(file_path_analisis).mkdir(parents=True, exist_ok=True)
data = pd.read_csv(file_path_data)

# === 2. Ambil kolom ===
strain = data['strain']
stress = data['stress']

# === 3. Plot grafik ===
plt.figure()
plt.plot(strain, stress)

# === 4. Label & judul ===
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve')

# === 5. Grid biar enak dibaca ===
plt.grid()
plt.yticks(np.arange(0, 600, 50))      # tiap 50 MPa
plt.xticks(np.arange(0, 0.2, 0.02))    # tiap 0.02 strain

# === 6. Tampilkan grafik ===
uts = stress.max()
uts_index = stress.idxmax()
uts_strain = strain[uts_index]

plt.savefig(file_path_curve)


#Analisis
with open(file_path_analisis2, "w") as f:
    f.write("=== HASIL ANALISIS MATERIAL ===\n\n")
    f.write(f"Material: {pilih_material}\n\n")
    f.write(f"UTS: {uts} MPa\n")
    f.write(f"Strain UTS: {uts_strain}\n")
    
plt.show()
