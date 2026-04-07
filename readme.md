This project is a Python-based tool for analyzing tensile test data.
It reads stress-strain data from CSV files, generates stress-strain curves, and extracts key material properties such as Ultimate Tensile Strength (UTS).

The program also automatically organizes outputs into structured folders for each material.

Features
-Load stress-strain data from CSV files
-Generate stress-strain plots automatically
-Customize axis scale for better visualization
-Calculate:
    -Ultimate Tensile Strength (UTS)
    -Strain at UTS
-Save:
    -Plot as .png
    -Analysis results as .txt
    -Automatically create folders for each material

Folder Structure

project/
│
├── stress_strain_data/
│   ├── steel.csv
│   ├── aluminum.csv
│
├── analysis_result/
│   ├── steel/
│   │   ├── steel.png
│   │   ├── steel.txt
│
└── main.py

CSV Format Example

strain,stress
0.000,0
0.001,200
0.002,400
...

HOW TO RUN
1.pip install pandas matplotlib numpy
2.Run the script(python main.py)
3.Input materials name

Output
1.Stress-Strain-Curve
2.Analysis-File
example:
=== MATERIAL ANALYSIS RESULT ===

UTS (Ultimate Tensile Strength): 550 MPa
Strain at UTS: 0.03


