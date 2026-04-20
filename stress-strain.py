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

# ====6 Analytics ======
uts = stress.max()
uts_index = stress.idxmax()
uts_strain = strain[uts_index]

# === Young's Modulus (ambil slope awal) ===
# asumsi linear di strain kecil (misal < 0.002)
elastic_region = strain < 0.002 # ACC
E = np.polyfit(strain[elastic_region], stress[elastic_region], 1)[0]


# === Yield Strength (offset 0.2%) ===
offset = 0.002
offset_line = E * (strain - offset)
# cari perpotongan
diff = stress - offset_line
yield_index = np.where(diff > 0)[0][0]
yield_strength = stress[yield_index]
yield_strain = strain[yield_index]

# === Fracture Point ===
fracture_stress = stress.iloc[-1]
fracture_strain = strain.iloc[-1]

# === Toughness (integral area bawah kurva) ===
toughness = np.trapezoid(stress, strain)

# === Resilience (area elastis saja) ===
resilience = np.trapezoid(stress[elastic_region], strain[elastic_region])
plt.savefig(file_path_curve)


#Analisis
with open(file_path_analisis2, "w") as f:
    f.write("=== HASIL ANALISIS MATERIAL ===\n\n")
    f.write(f"Material: {pilih_material}\n\n")
    f.write(f"UTS: {uts} MPa\n")
    f.write(f"Strain UTS: {uts_strain}\n")
    f.write(f"Young's Modulus: {E:.2f} MPa\n")
    f.write(f"Yield Strength: {yield_strength:.2f} MPa\n")
    f.write(f"Strain Yield: {yield_strain:.4f}\n")
    f.write(f"Fracture Stress: {fracture_stress:.2f} MPa\n")
    f.write(f"Fracture Strain: {fracture_strain:.4f}\n")
    f.write(f"Toughness: {toughness:.2f} MJ/m^3\n")
    f.write(f"Resilience: {resilience:.2f} MJ/m^3\n")

# === 6. Tampilkan grafik ===
plt.show()
