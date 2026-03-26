import random
from datetime import datetime
from fpdf import FPDF

class EmergencyKitGenerator:
    def __init__(self, family_size, days, hazard):
        self.family_size = family_size
        self.days = days
        self.hazard = hazard.lower().strip()
        self.date_generated = datetime.now().strftime("%B %d, 2026")
        
        self.categories = {
            "Hydration and Nutrition": [],
            "Medical and Hygiene": [],
            "Survival Gear": [],
            "Important Documents": []
        }
        
        self.tips = [
            "Rotate your food and water supplies every six months.",
            "Keep a pair of sturdy shoes near your bed for nighttime emergencies.",
            "Designate an out-of-area contact person to coordinate family check-ins.",
            "Text messages often transmit more reliably than voice calls during network congestion."
        ]

    def calculate_supplies(self):
        water_total = self.family_size * 4 * self.days
        food_total = self.family_size * 3 * self.days
        
        self.categories["Hydration and Nutrition"].extend([
            f"Water: {water_total} Liters (Total supply for {self.days} days)",
            f"Non-perishable food: {food_total} Meals",
            "Manual can opener and mess kits"
        ])

        self.categories["Medical and Hygiene"].extend([
            "Comprehensive First Aid Kit",
            "Prescription medications (Minimum 7-day supply)",
            "Sanitation supplies: Moist towelettes and waste bags"
        ])

        self.categories["Survival Gear"].extend([
            "Flashlight with extra batteries",
            "Battery-powered or hand-crank NOAA Weather Radio",
            "Multi-tool and heavy-duty duct tape"
        ])

        if "flood" in self.hazard:
            self.categories["Important Documents"].append("Waterproof sleeves for identification and insurance")
            self.categories["Survival Gear"].append("Rubber boots and life vests")
        elif "earthquake" in self.hazard:
            self.categories["Survival Gear"].append("Sturdy footwear and leather work gloves")
            self.categories["Survival Gear"].append("Emergency whistle for signaling")
        elif "fire" in self.hazard:
            self.categories["Medical and Hygiene"].append("N95 Respirator masks")
            self.categories["Survival Gear"].append("Emergency fire-retardant blanket")

    def generate_pdf(self, filename="SENTINEL-PREP-PLAN.pdf"):
        pdf = FPDF()
        pdf.add_page()

        # Header Section
        pdf.set_font("Arial", "B", 24)
        pdf.set_text_color(20, 40, 80)
        pdf.cell(200, 15, txt="SENTINEL-PREP ARCHITECT", ln=True, align="C")
        
        pdf.set_font("Arial", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(200, 10, txt=f"Date of Issue: {self.date_generated}", ln=True, align="C")
        pdf.ln(5)

        # Summary Row
        pdf.set_fill_color(240, 240, 240)
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 0, 0)
        summary = f"Household: {self.family_size} | Duration: {self.days} Days | Hazard Focus: {self.hazard.upper()}"
        pdf.cell(190, 12, txt=summary, ln=True, align="C", fill=True)
        pdf.ln(10)

        # Checklist Generation
        for cat, items in self.categories.items():
            if items:
                pdf.set_font("Arial", "B", 14)
                pdf.set_fill_color(220, 230, 240)
                pdf.cell(190, 10, txt=f" {cat}", ln=True, fill=True)
                pdf.ln(3)

                pdf.set_font("Arial", size=12)
                for item in items:
                    pdf.cell(190, 9, txt=f" [  ] {item}", ln=True)
                pdf.ln(6)

        # Emergency Contacts (The part you were missing)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(190, 10, txt="Emergency Contact Records (Hand-write below):", ln=True)
        pdf.set_draw_color(180, 180, 180)
        pdf.rect(10, pdf.get_y(), 190, 30) # Box for writing
        pdf.ln(35)

        # Random Strategic Tip
        pdf.set_font("Arial", "I", 11)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(190, 10, txt=f"Strategic Tip: {random.choice(self.tips)}", align="C")

        pdf.output(filename)
        print(f"\nSystem: Plan successfully generated as {filename}")

# --- HELPER FUNCTION FOR CLEAN INPUT ---
def get_clean_int(prompt):
    while True:
        val = input(prompt).strip()
        clean_val = "".join(filter(str.isdigit, val))
        if clean_val:
            return int(clean_val)
        print("Error: Input must be a numerical value (e.g., 4).")

# --- ACTUAL RUN COMMANDS ---
if __name__ == "__main__":
    print("\n--- Sentinel-Prep Initialization ---")
    p = get_clean_int("Enter Household Size: ")
    d = get_clean_int("Enter Duration (Days): ")
    h = input("Enter Primary Hazard (Flood/Earthquake/Fire): ")

    gen = EmergencyKitGenerator(p, d, h)
    gen.calculate_supplies()
    gen.generate_pdf()