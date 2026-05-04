from tensile_test import pilih_material as tt

print("="*50)
print("   MATERIAL PROPERTY ANALYZER")
print("="*50)
print("Analyze material behavior from Test Data")
print("\nAvailable Features:")
print("  1. Stress-Strain Analysis")
print("  2. Creep Analysis (Coming Soon)")
print("  3. Fatigue Analysis (Coming Soon)")
print("  0. Help")
print("="*50)

option = input("Select an option >> ")
if option == "1":
    print(tt())
elif option == "2":
    print("Work in progress")
elif option == "3":
    print("Work in progress")
elif option =="0":
    print("")
else:
    print("Pilihan tidak valid")