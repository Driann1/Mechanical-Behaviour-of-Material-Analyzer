def pilih_material():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from pathlib import Path

    material = input("Material apa yang ingin di pilih \n")

    file_path_analisis = f"analysis_result/{material}"
    file_path_analisis2 = f"{file_path_analisis}/{material}.txt"
    file_path_curve = f"{file_path_analisis}/{material}.png"
    file_path_data = f"stress_strain_data/{material}.csv"

    Path(file_path_analisis).mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(file_path_data)

    strain = data['strain']
    stress = data['stress']

    plt.figure()
    plt.plot(strain, stress)

    plt.xlabel('Strain')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve')

    plt.grid()
    plt.yticks(np.arange(0, 600, 50))
    plt.xticks(np.arange(0, 0.2, 0.02))

    uts = stress.max()
    uts_index = stress.idxmax()
    uts_strain = strain[uts_index]

    elastic_region = strain < 0.002
    E = np.polyfit(strain[elastic_region], stress[elastic_region], 1)[0]

    offset = 0.002
    offset_line = E * (strain - offset)
    diff = stress - offset_line
    yield_index = np.where(diff > 0)[0][0]
    yield_strength = stress[yield_index]
    yield_strain = strain[yield_index]

    fracture_stress = stress.iloc[-1]
    fracture_strain = strain.iloc[-1]

    toughness = np.trapezoid(stress, strain)
    resilience = np.trapezoid(stress[elastic_region], strain[elastic_region])

    plt.savefig(file_path_curve)

    with open(file_path_analisis2, "w") as f:
        f.write("=== HASIL ANALISIS MATERIAL ===\n\n")
        f.write(f"Material: {material}\n\n")
        f.write(f"UTS: {uts} MPa\n")
        f.write(f"Strain UTS: {uts_strain}\n")
        f.write(f"Young's Modulus: {E:.2f} MPa\n")
        f.write(f"Yield Strength: {yield_strength:.2f} MPa\n")
        f.write(f"Strain Yield: {yield_strain:.4f}\n")
        f.write(f"Fracture Stress: {fracture_stress:.2f} MPa\n")
        f.write(f"Fracture Strain: {fracture_strain:.4f}\n")
        f.write(f"Toughness: {toughness:.2f} MJ/m^3\n")
        f.write(f"Resilience: {resilience:.2f} MJ/m^3\n")

    plt.show()

