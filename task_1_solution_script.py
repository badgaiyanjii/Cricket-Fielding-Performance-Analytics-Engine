"""
Task 1: Core Python Fundamentals
ShadowFox Python Development Internship
Author: Aanya Badgaiyan
"""

# ==========================================
# 1. Variables & Mathematical Operations
# ==========================================
pi = 22 / 7
print(f"Value of pi: {pi}")
print(f"Data type of pi: {type(pi)}")

# Simple Interest Calculation
principal = 50000.0
rate = 7.5
time_years = 3
simple_interest = (principal * rate * time_years) / 100
print(f"Simple Interest for 3 years: INR {simple_interest:.2f}\n")

# ==========================================
# 2. Number Representations & Formatting
# ==========================================
number = 145
print(f"Octal representation of {number}: {format(number, 'o')}")

# Circle geometry & Pond water volume
radius = 84
pi_approx = 3.14
pond_area = pi_approx * (radius ** 2)
water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter
print(f"Pond Surface Area: {pond_area:.2f} sq.m")
print(f"Total Water Volume (Integer): {int(total_water)} Liters\n")

# ==========================================
# 3. Justice League List Operations
# ==========================================
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(f"Initial Justice League: {justice_league}")
print(f"Member Count: {len(justice_league)}")

# Add Batgirl & Nightwing
justice_league.extend(["Batgirl", "Nightwing"])

# Move Wonder Woman to index 0 as leader
justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))

# Move Superman between Aquaman and Flash
justice_league.remove("Superman")
flash_idx = justice_league.index("Flash")
justice_league.insert(flash_idx + 1, "Superman")

# Reset with new squad and sort alphabetically
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print(f"Sorted New Roster: {justice_league}")
print(f"New Elected Leader (Index 0): {justice_league[0]}\n")

# ==========================================
# 4. Conditionals: BMI Classifier
# ==========================================
def classify_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi >= 30:
        return bmi, "Obesity"
    elif bmi >= 25:
        return bmi, "Overweight"
    elif bmi >= 18.5:
        return bmi, "Normal"
    else:
        return bmi, "Underweight"

sample_bmi, category = classify_bmi(68, 1.72)
print(f"Sample BMI: {sample_bmi:.2f} -> Category: {category}\n")