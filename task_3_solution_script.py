"""
Task 3: Capstone IPL Cricket Fielding Performance Evaluation
ShadowFox Python Development Internship
Author: Aanya Badgaiyan
"""

import pandas as pd

def calculate_fielding_ps(row):
    """
    Computes Fielding Performance Score (PS):
    PS = (CP*1) + (GT*1) + (C*3) - (DC*3) + (ST*3) + (RO*3) - (MRO*2) + (DH*2) + RS
    """
    ps = (
        (row["CP"] * 1) +
        (row["GT"] * 1) +
        (row["C"] * 3) -
        (row["DC"] * 3) +
        (row["ST"] * 3) +
        (row["RO"] * 3) -
        (row["MRO"] * 2) +
        (row["DH"] * 2) +
        row["RS"]
    )
    return ps

def assign_tier(score):
    if score >= 11:
        return "Tier 1 (Elite)"
    elif score >= 10:
        return "Tier 1 (High Impact)"
    elif score >= 8:
        return "Tier 2 (Reliable Anchor)"
    elif score >= 5:
        return "Tier 3 (Moderate)"
    else:
        return "Tier 4 (Deficit/Needs Work)"

# Match Fielding Data: Delhi Capitals (IPL Match #2367)
raw_data = {
    "Player Name": [
        "Yash Dhull",
        "Axar Patel",
        "Rilee Rossouw",
        "Aman Khan",
        "Kuldeep Yadav",
        "Lalit Yadav",
        "Phil Salt"
    ],
    "Position": [
        "Covers",
        "Point",
        "Short Mid-Wicket",
        "Long Off",
        "Short Mid-Wicket",
        "Cover Point",
        "Wicketkeeper"
    ],
    "CP": [3, 2, 2, 4, 3, 1, 1],   # Clean Picks
    "GT": [1, 3, 1, 1, 0, 2, 2],   # Good Throws
    "C":  [2, 1, 1, 0, 1, 1, 0],   # Catches
    "DC": [0, 0, 0, 0, 1, 0, 1],   # Dropped Catches
    "ST": [0, 1, 0, 0, 0, 0, 0],   # Stumpings
    "RO": [0, 0, 0, 1, 0, 0, 1],   # Run Outs
    "MRO":[1, 0, 0, 0, 0, 0, 0],   # Missed Run Outs
    "DH": [0, 0, 1, 0, 1, 1, 0],   # Direct Hits
    "RS": [3, 0, 2, 1, 4, -2, -1]  # Net Runs Saved
}

def main():
    df = pd.DataFrame(raw_data)
    df["Performance Score (PS)"] = df.apply(calculate_fielding_ps, axis=1)
    df["Status"] = df["Performance Score (PS)"].apply(assign_tier)
    df = df.sort_values(by="Performance Score (PS)", ascending=False).reset_index(drop=True)

    print("=========================================================================================")
    print("                 DELHI CAPITALS - IPL FIELDING PERFORMANCE MATRIX                       ")
    print("=========================================================================================")
    print(df[["Player Name", "Position", "Performance Score (PS)", "Status"]].to_string(index=False))
    print("=========================================================================================\n")

if __name__ == "__main__":
    main()