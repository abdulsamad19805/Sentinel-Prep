# Sentinel-Prep: Emergency Kit Architect 

A Python-based utility designed to generate personalized emergency preparedness plans. This tool automates the creation of survival supply checklists tailored to household size, duration, and specific environmental hazards.

##  Project Overview
As a Computer Science student, I developed this project to apply programming logic to emergency preparedness. The script processes user inputs to calculate essential resources and exports a professional, categorized PDF plan.

##  Technical Highlights
- **Dynamic Resource Logic:** Calculates water (1 gallon/person/day) and food requirements using linear scaling.
- **Data Mapping:** Uses nested dictionaries for efficient retrieval of hazard-specific gear (Flood, Earthquake, or Fire).
- **Automated PDF Export:** Integrates the `fpdf` library to transform terminal data into structured, printable documents.
- **Input Sanitization:** Implements filtering to ensure data integrity before document compilation.

##  Tech Stack
- **Language:** Python 3.9+
- **Primary Library:** `fpdf`
- **Concepts:** Data Structures (Dictionaries), File I/O, Error Handling.

##  How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/abdulsamad19805/Sentinel-Prep.git](https://github.com/abdulsamad19805/Sentinel-Prep.git)
