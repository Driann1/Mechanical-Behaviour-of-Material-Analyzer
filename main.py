from stress_strain import pilih_material as stress_strain

print("Welcome to MBOM \n how can i help you? ")
option = input("0. Help \n1. Material Stress Strain Analysis\n2. Material Creep Test Analysis\n3. Material Fatigue Test Analysis\nYour Option:")

if option == "1":
    print(stress_strain())
elif option == "2":
    print("Work in progress")
elif option == "3":
    print("Work in progress")
else:
    print("Pilihan tidak valid")