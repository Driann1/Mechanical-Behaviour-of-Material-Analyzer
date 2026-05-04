# MATERIAL PROPERTY ANALYZER — DOCUMENTATION

## 1. Overview

**Material Property Analyzer** is a Python-based command-line tool designed to analyze material behavior using stress-strain test data.
The program processes CSV data and automatically calculates key mechanical properties, generates a stress-strain curve, and outputs a structured analysis report.


## 2. How It Works
The system follows a simple pipeline:

1. User selects analysis type
2. User selects material category
3. User inputs material code
4. Program reads CSV data
5. Data is processed and analyzed
6. Outputs are generated:
   * Graph (PNG)
   * Analysis report (TXT)

## 3. Flow Diagram
START
  ↓
Display Menu
  ↓
User Selects Option
  ↓
[If Option = 1]
  ↓
Material Selection
  ↓
Input Material Code
  ↓
Load CSV Data
  ↓
Process Data:
  - Stress-Strain Curve
  - UTS
  - Young’s Modulus
  - Yield Strength
  - Toughness & Resilience
  ↓
Save Output Files
  ↓
Display Graph
  ↓
END



## 4. Features

### 4.1 Stress-Strain Analysis

* Reads experimental data from CSV
* Generates stress-strain curve
* Computes:

  * Ultimate Tensile Strength (UTS)
  * Strain at UTS
  * Young’s Modulus
  * Yield Strength (0.2% offset method)
  * Fracture point
  * Toughness
  * Resilience

### 4.2 Planned Features

* Creep Analysis (Work in Progress)
* Fatigue Analysis (Work in Progress)



## 5. File Structure
project/
│
├── main.py
├── stress_strain.py
│
├── Test_Data/
│   └── stress_strain_data/
│       ├── Metal/
│       ├── Ceramics/
│       ├── Polymer/
│       └── Composite/
│
├── analysis_result/
│   └── (auto-generated)




## 6. Adding or Editing Data
### CSV File Format
Each material must have a CSV file with the following columns:

strain,stress
0.000,0
0.001,200
0.002,350


### Naming Convention
When adding new data we recommend using this format:

The initial of Material + Specifics name + suffix number (and put the detail in the material information file)

Ex:
Metal Non Ferrous 1 = MNF1
this just makes easier when running the code

NOTE: you can still name it however you want!

## 7. How to Use
### Step 1: Run the Program python "main.py"

### Step 2: Select Feature
1 → Stress-Strain Analysis
2 → Creep Analysis
3 → Fatigue Analysis
0 → Help

### Step 3: Select Material Type

[1] Metal
[2] Ceramics
[3] Polymer
[4] Composite


### Step 4: Input Material Code

Example:
MNF1

### Step 5: View Results
The program will:

* Display stress-strain graph
* Save outputs automatically


## 8. Output Files

Location:
analysis_result/{Material}/{MaterialCode}/

Generated files:

* {MaterialCode}.png → Stress-Strain graph
* {MaterialCode}.txt → Analysis report


## 9. Calculation Methods
### 9.1 Ultimate Tensile Strength (UTS)
Maximum stress value:
UTS = max(stress)

### 9.2 Young’s Modulus
Calculated from linear elastic region:
E = slope of stress-strain curve (strain < 0.002)


### 9.3 Yield Strength (0.2% Offset)
* Offset line is generated
* Intersection with curve determines yield point

### 9.4 Toughness
Area under the curve:
Toughness = ∫ stress d(strain)

### 9.5 Resilience
Elastic region energy:
Resilience = ∫ stress d(strain) (elastic region only)


## 10. Error Handling

Common issues:
### File Not Found
* Ensure CSV file exists
* Check correct material code

### Invalid Input
* Input must match menu options

### Data Format Error
* CSV must contain:
  * strain
  * stress

## 11. Limitations

* Only supports stress-strain analysis (for now)
* Assumes clean experimental data
* Limited validation for incorrect datasets

## 12. Future Improvements

* Add creep and fatigue analysis
* GUI interface
* Automatic material detection
* Advanced data validation
* Multi-material comparison

## 13. Conclusion
This tool demonstrates how raw experimental data can be transformed into meaningful engineering insights using Python.
It is designed as a foundational project for further development in material analysis and engineering software tools.


END OF DOCUMENTATION
